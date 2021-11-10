import pandas as pd
from data.data_tools.generate_testing_dataset import df
from shapely.geometry import Polygon
from app_here.utilities.map_info.json_map_data import polys, county_names
import math

def pipeline_model(df, obs):
    """Model to generate on the spot """
    df_c = df.copy()
    for x in obs.columns:
        df_c = df_c.loc[df_c[x] == obs[x][0]]

    return df_c


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

    refs = [36.981528, -91.511353]
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


def regional_search(lat_dd, long_dd, man_dd, model_dd, fuel_dd, type_dd,
                  transmission_dd, color_dd, condition_dd, cylinder_dd, year_dd,
                  miles_dd, drive_dd):
    d = {0: 'manufacturer', 1: 'model', 2: 'fuel', 3: 'type', 4: 'transmission',
         5: 'paint_color', 6: 'condition', 7: 'cylinders', 8: 'year', 9: 'odometer',
         10: 'drive'}
    cols_check = [man_dd, model_dd, fuel_dd, type_dd,
                  transmission_dd, color_dd, condition_dd, cylinder_dd, year_dd,
                  miles_dd, drive_dd]
    cols_drop = []
    obs = pd.DataFrame(index=[0])
    for i, x in enumerate(cols_check):
        if x is None:
            cols_drop.append(d[i])
        else:
            obs[d[i]] = x
    index_of_df = set()
    for j in range(len(df)):
        index_of_df.add(j)
    length = 0
    factor = 1
    while length < 120 and factor < 3:
        max_dist = 60 * factor
        factor += 1
        index_directory = []
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, max_dist)
        copy_index = index_of_df.copy()
        for i in index_of_df:
            if df.iloc[i]['county'] in intersect:
                index_directory.append(i)
                copy_index.remove(i)
        index_of_df = copy_index
        df_to_check = df.iloc[index_directory]
        df_to_show = pipeline_model(df_to_check, obs)
        length = len(df_to_show)
    answer = {'min': df_to_show['price'].min(), 'avg': df_to_show['price'].mean(), 'max': df_to_show['price'].max()}

    return answer
