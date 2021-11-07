from main_app.map_info.json_map_data import topojson
import folium
import math
from main_app.map_info.json_map_data import polys, county_names
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

    refs = [36.981528, -91.511353]
    lat_ratio = ((41.148339 - 36.981528) / (2*3344))
    long_ratio = ((-89.638487 + 91.511353) / (2*1061))
    radius = radius / 70
    radius = round(radius / lat_ratio)
    lat_pre = abs(refs[0] - lat)
    long_pre = abs(refs[1] - long)
    y_coord = round(long_pre / long_ratio)
    x_coord = round(lat_pre / lat_ratio)
    center = [y_coord, x_coord]
    coords = get_all_circle_coords(center[0], center[1], radius, 60)
    circle = Polygon(coords)
    intersectors = set()
    for i, shape in enumerate(polys):
        if shape.intersects(circle):
            intersectors.add(county_names[i])
    return intersectors


# function for creating map
def create_map(df, lat, long, radius):
    radius = (radius / 0.621371) * 1000

    m = folium.Map(width=800,
                   height=800,
                   location=[lat, long],
                   tiles="cartodbpositron",
                   zoom_start=7,
                   )
    if not df is None:
        for i in range(len(df)):
            loc = [df.iloc[i]['lat'], df.iloc[i]['long']]
            folium.CircleMarker(
                name='markers',
                location=loc,
                radius=2,
                weight=5,
                color='green'
            ).add_to(m)

        folium.Circle(
            name='radius',
            radius=radius,
            location=[lat, long],
            popup="Search Area",
            color="red",
            fill=True,
            fill_color='red'
        ).add_to(m)

    # folium.GeoJson(url, name="geojson").add_to(m)

    folium.TopoJson(
        topojson,
        "objects.cb_2015_illinois_county_20m",
        name="car prospects",

    ).add_to(m)

    folium.LayerControl().add_to(m)

    return m._repr_html_()
