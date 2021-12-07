import pandas as pd
from shapely.geometry import Polygon, Point
from GraphQL_Interface.map_data.json_map_data import polys, refs, county_names
import math
import mysql.connector
import os
from .schema_components import Vehicle, Dealer
from dotenv import load_dotenv

load_dotenv()


def get_vehicle(id):
    """Simple function to return Vehicle from Database. Input vehicle id."""

    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query = f"""SELECT * FROM vehicles WHERE id = {id}"""
        resp = pd.read_sql(query, cnx).to_dict()
        vehicle_object = Vehicle(
            id=resp['id'][0],
            year=resp['year'][0],
            manufacturer=resp['manufacturer'][0],
            model=resp['model'][0],
            condition=resp['cond'][0],
            odometer=resp['odometer'][0],
            type=resp['type'][0],
            transmission=resp['transmission'][0],
            drive=resp['drive'][0],
            color=resp['paint_color'][0],
            price=resp['price'][0],
            cylinders=resp['cylinders'][0],
            VIN=resp['VIN'][0],
            dealer_id=resp['dealer_ID'][0]
        )
    finally:
        cnx.close()
    return vehicle_object


def get_dealer(id):
    """simple function to return dealer. Input dealer ID."""

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


def dealer_retrieval(counties):
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


def vehicle_query(ids, fields, values, table_columns=None):
    """function for formatting query and return data from database"""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        if table_columns is None:
            query_p1 = """SELECT * FROM vehicles WHERE """
        else:
            query_p1 = """SELECT"""
            cap = """ FROM vehicles WHERE"""
            for col in table_columns:
                query_p1 += ' ' + col + ','
            query_p1 = query_p1[:-1]
            query_p1 += cap
        query_p2 = """ dealer_ID ="""
        for count in ids['id'][:-1]:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1 + query_p2 + ' ' + "'" + str(ids['id'][len(ids) - 1]) + "'"
        for i in range(len(fields)):
            query += f""" AND {fields[i]} = '{values[i]}'"""
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


def search_function(long_dd, lat_dd, data, search):
    def option_1(long_dd, lat_dd, data):
        """for basic radius search"""
        lat_adj = (lat_dd * 69)
        long_adj = (long_dd * 54.6)
        final_distance = data['radius']
        del data['radius']
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT id FROM dealers WHERE """ \
                    f"""(SQRT((((c1*69) - {lat_adj}) * ((c1*69) - {lat_adj}))""" \
                    f"""+ (((c2*54.6) - {long_adj})*((c2*54.6) - {long_adj}))) < {final_distance}); """
            ids = pd.read_sql(query, cnx)
            sql_return = vehicle_query(ids, [x for x in data.keys()],
                                       [x for x in data.values()], table_columns=['id'])
        finally:
            cnx.close()
        return [item for item in sql_return['id']]

    def option_2(long_dd, lat_dd, data):
        """for regional search"""
        radius = data['radius']
        del data['radius']
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, radius)
        ids = dealer_retrieval(intersect)
        sql_return = vehicle_query(ids, [x for x in data.keys()],
                                   [val for val in data.values()],
                                   table_columns=['id'])
        return [item for item in sql_return['id']]

    if search == 'RADIUS':
        return option_1(long_dd, lat_dd, data)
    elif search == 'REGIONAL':
        return option_2(long_dd, lat_dd, data)
    else:
        return 'not yet implemented'


def regional_search(data, search=None):
    """begininning of regional search"""

    lat_dd = data['lat']
    long_dd = data['long']
    # only for now.... removing year and odometer from selection criteria
    del data['long']
    del data['lat']
    if 'year' in data:
        del data['year']
    if 'odometer' in data:
        del data['odometer']

    length = 0
    factor = 1
    if search is None:
        while length < 25 and factor < 3:
            max_dist = 60 + (30 * factor)
            factor += 1
            intersect, circle = find_intersecting_counties(lat_dd, long_dd, max_dist)
            ids = dealer_retrieval(intersect)
            sql_return = vehicle_query(ids, [x for x in data.keys()],
                                       [val for val in data.values()])
            length = len(sql_return)

        answer = {'min': sql_return['price'].min(), 'avg': sql_return['price'].mean(), 'max': sql_return['price'].max()}

        return answer
    else:
        final_return = search_function(long_dd, lat_dd, data, search)
        return final_return
