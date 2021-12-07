import pandas as pd
from shapely.geometry import Polygon, Point
from GraphQL_Interface.map_data.json_map_data import polys, refs, county_names
import math
import mysql.connector
import os
from .schema_components import Vehicle, Dealer
from dotenv import load_dotenv

load_dotenv()

dealers_cache = {}

def get_vehicle(id, data=None):
    """Simple function to return Vehicle from Database. Input vehicle id."""
    if data is not None:
        resp = data.to_dict()
    else:
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM vehicles WHERE id = {id}"""
            resp = pd.read_sql(query, cnx).iloc[0].to_dict()
        finally:
            cnx.close()
    vehicle_object = Vehicle(
        id=resp['id'],
        year=resp['year'],
        manufacturer=resp['manufacturer'],
        model=resp['model'],
        condition=resp['cond'],
        odometer=resp['odometer'],
        type=resp['type'],
        transmission=resp['transmission'],
        drive=resp['drive'],
        color=resp['paint_color'],
        price=resp['price'],
        cylinders=resp['cylinders'],
        VIN=resp['VIN'],
        dealer_id=resp['dealer_ID']
    )

    return vehicle_object


def get_dealer(id, data=None):
    """simple function to return dealer. Input dealer ID."""
    if data is not None:
        pass
        return
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query = f"""SELECT * FROM dealers WHERE id = '{id}'"""
        resp = pd.read_sql(query, cnx).to_dict()
        dealer_object = Dealer(
            id=resp['id'][0],
            city=resp['city'][0],
            name=resp['name'][0]
        )
    finally:
        cnx.close()
    return dealer_object


def dealer_query(counties):
    """function for formatting query"""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query_p1 = """SELECT * FROM dealers WHERE"""
        query_p2 = """ county ="""
        for count in counties:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1[:-3]
        dealers = pd.read_sql(query, cnx)

    finally:
        cnx.close()
    return dealers


def vehicle_query(ids):
    """function for formatting query and return data from database"""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))

        query_p1 = """SELECT * FROM vehicles WHERE """
        query_p2 = """ dealer_ID ="""
        for count in ids['id'][:-1]:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1 + query_p2 + ' ' + "'" + str(ids['id'][len(ids) - 1]) + "'"
        data = pd.read_sql(query, cnx)
    finally:
        cnx.close()
    return data


def get_circle_coord(theta, x_center, y_center, radius):
    x = radius * math.cos(theta) + x_center
    y = radius * math.sin(theta) + y_center
    return [round(x), round(y)]


# This function gets all the pairs of coordinates
def get_all_circle_coords(x_center, y_center, radius, n_points):
    thetas = [i / n_points * math.tau for i in range(n_points + 1)]
    circle_coords = [get_circle_coord(theta, x_center, y_center, radius) for theta in thetas]
    return circle_coords


def find_intersecting_counties(lat, long, radius):
    """Function to return intersecting counties"""

    lat_ratio = ((41.148339 - 36.981528) / 3344)
    long_ratio = ((-89.638487 + 91.511353) / 1061)
    radius = radius / 69
    radius = int(radius / lat_ratio)
    lat_pre = abs(refs[1] - lat)
    long_pre = abs(refs[0] - long)
    y_coord = int(long_pre / long_ratio)
    x_coord = int(lat_pre / lat_ratio)
    center = [y_coord, x_coord]
    coords = get_all_circle_coords(center[0], center[1], radius, 60)
    circle = Polygon(coords)
    intersectors = set()
    for i, shape in enumerate(polys):
        if shape.intersects(circle):
            intersectors.add(county_names[i])
    coords_real = []
    for pos in coords:
        y = pos[0] * long_ratio
        x = pos[1] * lat_ratio
        coords_real.append([y + refs[1], x + refs[0]])
    circle_geo = Polygon(coords_real)

    return intersectors, circle_geo


def search_function(data):
    print('found search function')
    def option_1(long_dd, lat_dd, data):
        print('made it to the correct function block', data)
        """for basic radius search"""
        lat_adj = (lat_dd * 69)
        long_adj = (long_dd * 54.6)
        final_distance = data['radius']
        del data['radius']
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM dealers WHERE """ \
                    f"""(SQRT((((c1*69) - {lat_adj}) * ((c1*69) - {lat_adj}))""" \
                    f"""+ (((c2*54.6) - {long_adj})*((c2*54.6) - {long_adj}))) < {final_distance}); """
            ids = pd.read_sql(query, cnx)
            sql_return = vehicle_query(ids)
        finally:
            cnx.close()
        return [item for item in sql_return['id']]

    def option_2(long_dd, lat_dd, data):
        """for regional search"""
        radius = data['radius']
        print('found option 2, :\n', data)
        del data['radius']
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, radius)
        ids = dealer_query(intersect)
        sql_return = vehicle_query(ids)
        vehicle_lists = []
        for i in range(len(sql_return)):
            row = sql_return.iloc[i]
            vehicle_lists.append(get_vehicle(row['id'], row))
        return vehicle_lists



    long_dd = data['long']
    lat_dd = data['lat']
    search = data['search_cat']
    del data['long']
    del data['lat']
    del data['search_cat']
    if search == 'RADIUS':
        return option_1(long_dd, lat_dd, data)
    elif search == 'REGION':
        return option_2(long_dd, lat_dd, data)
    else:
        return 'not yet implemented'
