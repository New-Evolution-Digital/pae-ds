import pandas as pd
import numpy as np
from shapely.geometry import Polygon, Point
from app_here.utilities.map_info.json_map_data import polys, refs
# from datah.data_tools.generate_testing_dataset import call_df
import math


# functions to determine points of circle
# This function gets just one pair of coordinates based on the angle theta
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
    print(refs)
    lat_ratio = ((41.148339 - 36.981528) / 3344)
    long_ratio = ((-89.638487 + 91.511353) / 1061)
    radius = radius / 69
    radius = int(radius / lat_ratio)
    lat_pre = abs(refs[0] - lat)
    long_pre = abs(refs[1] - long)
    y_coord = int(long_pre / long_ratio)
    x_coord = int(lat_pre / lat_ratio)
    center = [y_coord, x_coord]
    coords = get_all_circle_coords(center[0], center[1], radius, 60)
    circle = Polygon(coords)
    intersectors = []
    for i, shape in enumerate(polys):
        if shape.intersects(circle):
            intersectors.append(shape)
    coords_real = []
    for pos in coords:
        y = pos[0] * long_ratio
        x = pos[1] * lat_ratio
        coords_real.append([y + refs[1], x + refs[0]])
    circle_geo = Polygon(coords_real)
    print(len(intersectors))
    print(len(polys))
    return intersectors, circle_geo


def regional_search(data):
    df = call_df()
    for feature, value in data.items():
        if feature != 'longitude' and feature != 'latitude' and feature != 'odometer' and feature != 'year':
            df = df.loc[df[feature] == value]
    try:
        long_dd = data['longitude']
    except:
        return 'error, no longitudinal coordinate!!!!'
    try:
        lat_dd = data['latitude']
    except:
        return 'error, no latitudinal coordinate!!!!'

    length = 0
    factor = 1
    while length < 10 and factor < 3:
        max_dist = 60 + (30 * factor)
        factor += 1
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, max_dist)
        ind_to_show = []
        for i in range(len(df)):
            coords = (df.iloc[i]['latitude'], df.iloc[i]['longitude'])
            point = Point(coords)
            for shape in intersect:
                if point.within(shape):
                    ind_to_show.append(i)
                    break
        length = len(ind_to_show)
    df_to_show = df.iloc[ind_to_show]
    answer = {'min': df_to_show['price'].min(), 'avg': df_to_show['price'].mean(), 'max': df_to_show['price'].max()}

    return answer


def option_1(data, df):
    dfc = df.copy()
    lat = data['latitude']
    long = data['longitude']
    max_dist = data['radius']
    intersect, circle = find_intersecting_counties(lat, long, max_dist)
    ind_to_show = []
    for i in range(len(dfc)):
        coords = (dfc['latitude'], dfc['longitude'])
        point = point(coords)
        for shape in intersect:
            if point.within(shape):
                ind_to_show.append(i)
                break
    df_to_show = dfc.iloc[ind_to_show]

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
    for feature, value in data.items():
        if feature != 'longitude' and feature != 'latitude' and feature != 'odometer' and feature != 'year':
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
