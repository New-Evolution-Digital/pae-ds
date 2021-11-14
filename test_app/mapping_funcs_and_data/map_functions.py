from test_app.mapping_funcs_and_data.json_map_data import topojson, polys, county_names, refs
import folium
import math
from shapely.geometry import Polygon


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


# developing function to return intersections of circle radius
# enter radius in miles
def find_intersecting_counties(lat, long, radius):
    """Function to return intersecting counties"""
    refs1 = refs.copy()
    print(refs1)
    print(lat, long)
    lat_ratio = ((41.148339 - 36.981528)/3344)
    long_ratio = ((-89.638487 + 91.511353)/1061)
    radius = radius/69
    radius = int(radius/lat_ratio)
    lat_pre = abs(refs[0] - lat)
    long_pre = abs(refs[1] - long)
    y_coord = int(long_pre/long_ratio)
    x_coord = int(lat_pre/lat_ratio)
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


# function for creating map
def create_map(df, lat, long, circle):

    m = folium.Map(width=800,
                   height=800,
                   location=[lat, long],
                   tiles="cartodbpositron",
                   zoom_start=7,
                   )
    if not df is None:
        for i in range(len(df)):
            loc = [df.iloc[i]['latitude'], df.iloc[i]['longitude']]
            folium.CircleMarker(
                name='markers',
                location=loc,
                radius=2,
                weight=5,
                color='green'
            ).add_to(m)

        if type(circle) == int:

            radius = (circle / 0.621371) * 1000
            folium.Circle(
                name='radius',
                radius=radius,
                location=[lat, long],
                popup="Search Area",
                color="red",
                fill=True,
                fill_color='orange'
            ).add_to(m)
        else:
            print(circle)
            folium.Choropleth(geo_data=circle, name="radius", line_color='orange', fill_color='orange').add_to(m)

    folium.TopoJson(
        topojson,
        "objects.cb_2015_oregon_county_20m",
        name="car prospects",

    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m._repr_html_()

