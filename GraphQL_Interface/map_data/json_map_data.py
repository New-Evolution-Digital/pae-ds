import requests
import json
import numpy as np
from shapely.geometry import Polygon

# url for illinois county polygons. Replacebale by any other topojson of zip
# or county mappings with tweaking of below code

url = (
    'https://raw.githubusercontent.com/deldersveld/topojson/master/countries/us-states/OR-41-oregon-counties.json'
)

topojson = json.loads(requests.get(url).text)
refs1 = topojson['transform']['translate'][0]
refs2 = topojson['transform']['translate'][1]
refs = [refs1, refs2]
scale = topojson['transform']['scale']
beta = topojson['arcs']
polys = []
county_names = []

for i, x in enumerate(topojson['objects']['cb_2015_oregon_county_20m']['geometries']):
    poly_shape = []
    for y in x['arcs'][0]:
        if y < 0:
            temp = []
            y = abs(y + 1)
            arc_ind = beta[y].copy()
            ref = np.array(arc_ind[0])
            temp.append(ref)
            for j in range(1, len(arc_ind)):
                ref = ref + (np.array(arc_ind[j]))
                temp.append(ref)
            for zed in reversed(temp):
                poly_shape.append(zed)
        else:
            arc_ind = beta[y].copy()
            ref = np.array(arc_ind[0])
            poly_shape.append(ref)
            for j in range(1, len(arc_ind)):
                ref = ref + (np.array(arc_ind[j]))
                poly_shape.append(ref)
    shape_final = Polygon(poly_shape)
    polys.append(shape_final)
    county_names.append(x['properties']['NAME'])
