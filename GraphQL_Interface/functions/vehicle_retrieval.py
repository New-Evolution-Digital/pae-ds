import pandas as pd
import numpy as np
from shapely.geometry import Polygon, Point
from webapp.utilities.map_info.json_map_data import polys, refs, county_names
from webapp.datah.data_tools.generate_testing_dataset import call_df
import math
import mysql.connector
import os


# functions to determine points of circle
# This function gets just one pair of coordinates based on the angle theta

def dealer_retrieval(counties):
    """function for formatting query"""
    print('\n\n\ncommence dealer_retrieval stage')
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'), port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        print('checking connection..... \n\n',
              'mustve worked I guess.. \n\n\n')
        query_p1 = """SELECT id FROM dealers WHERE"""
        query_p2 = """ county ="""
        print('check status of counties: \n',
              counties)
        for count in counties:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1[:-3]
        print('check for errors in query: \n',
              query)
        dealers = pd.read_sql(query, cnx)
        print('checking dealers: \n',
              len(dealers))
    finally:
        cnx.close()
    return dealers


def vehicle_query(ids, fields, values):
    """function for formatting query and return data from database"""

    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'), port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query_p1 = """SELECT * FROM vehicles WHERE """
        query_p2 = """ dealer_ID ="""
        for count in ids['id'][:-1]:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1 + query_p2 + ' ' + "'" + str(ids['id'][len(ids)-1]) + "'"
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


def regional_search(data):
    """begininning of regional search"""

    lat_dd = data['lat']
    long_dd = data['long']
    print('just inside the call block, heres lat and long: \n',
          str(lat_dd) + ' ' + str(long_dd))
    # only for now.... removing year and odometer from selection criteria
    del data['long']
    del data['lat']
    if 'year' in data:
        del data['year']
    if 'odometer' in data:
        del data['odometer']
    print('deletion successful: \n',
          data)
    ###################### for now ###################################
    length = 0
    factor = 1
    while length < 10 and factor < 3:
        max_dist = 60 + (30 * factor)
        factor += 1
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, max_dist)
        print('interesection check: \n',
              len(intersect))
        ids = dealer_retrieval(intersect)
        sql_return = vehicle_query(ids, [x for x in data.keys()], [val for val in data.values()])
        length = len(sql_return)
    print('verifying sql_return dataframe: \n',
          len(sql_return))
    answer = {'min': sql_return['price'].min(), 'avg': sql_return['price'].mean(), 'max': sql_return['price'].max()}

    return answer


def option_1(data, df):
    dfc = df.copy()
    lat = data['latitude']
    long = data['longitude']
    max_dist = data['radius']
    intersect, circle = find_intersecting_counties(lat, long, max_dist)
    ind_to_show = []
    for i in range(len(dfc)):
        if dfc.iloc[i]['county'] in intersect:
            ind_to_show.append(i)
    df_to_show = dfc.iloc[ind_to_show]
    print(len(df_to_show))
    df_to_show.fillna('null value')

    return df_to_show.to_dict()


def option_2(data, df):
    to_show = []
    dfc = df.copy()
    max_dist = data['radius']
    lat = data['latitude']
    long = data['longitude']
    for i in range(len(df)):
        alpha = np.sqrt(
            ((df.iloc[i]['lat'] * 69) - (lat * 69)) ** 2 + ((df.iloc[i]['long'] * 54.6) - (long * 54.6)) ** 2)
        if not alpha > max_dist:
            to_show.append(i)
    df_to_show = dfc.iloc[to_show]
    return df_to_show.to_dict()


def option_3(data, df):
    to_show = []
    dfc = df.copy()
    max_dist = data['radius']
    lat = data['latitude']
    long = data['longitude']
    # homework for tomorrow:
    # need to add in formula to determine cheaper cars based on standard deviation threshold, then
    # add cheaper cars into the listing return for the customer
    for i in range(len(df)):
        alpha = np.sqrt(
            ((df.iloc[i]['lat'] * 69) - (lat * 69)) ** 2 + ((df.iloc[i]['long'] * 54.6) - (long * 54.6)) ** 2)
        if not alpha > max_dist:
            to_show.append(i)
    df_to_show = dfc.iloc[to_show]

    return df_to_show.to_dict()


def listing_retrieval(data):
    df = call_df()
    features_to_skip = ['longitude', 'latitude', 'miles', 'year', 'radius', 'option']
    skip_keys = set()
    for feature in features_to_skip:
        skip_keys.add(feature)
    for feature, value in data.items():
        if feature not in skip_keys:
            df = df.loc[df[feature] == value]
    try:
        data['longitude']
    except:
        return 'error, no longitudinal coordinate!!!!'
    try:
        data['latitude']
    except:
        return 'error, no latitudinal coordinate!!!!'

    try:
        if data['option'] == 1:
            return option_1(data, df)
        elif data['option'] == 2:
            return option_2(data, df)
        else:
            return option_3(data, df)
    except:
        return option_1(data, df)
