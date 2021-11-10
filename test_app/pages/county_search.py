from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output, State
from test_app.mapping_funcs_and_data.map_functions import create_map, find_intersecting_counties
from app import app


df = pd.read_csv('modified_csv')
center_lat = df['lat'].sum() / len(df)
center_long = df['long'].sum() / len(df)

layout = html.Div(children=[

    html.Div(className='row',
             children=[
                 html.Div(
                     html.H6(children="Latitude:")
                 ),
                 dcc.Input(id="lat_dd", placeholder='enter here', type="number", value=40.28),
                 html.Br(),
                 html.P(id="output")
             ]),
    html.Div(className='row',
             children=[
                 html.Div(
                     html.H6(children="Longitude:")
                 ),
                 dcc.Input(id="long_dd", placeholder='numer_here', type="number", value=-89.39),
                 html.Br(),
                 html.P(id="output")
             ]),
    html.Div(className='row', children=[
        html.Div(children=[
            html.Iframe(id='MapPlot2', srcDoc=create_map(None, center_lat, center_long, 0), width='100%', height=600)
        ])
    ]),
    html.Div(className='row', children=[
        html.Button('Fetch Cars', id='submit-val', n_clicks=0)
    ])
]
)


@app.callback(
    Output('MapPlot2', 'srcDoc'),
    [Input('submit-val', 'n_clicks'),
     State('lat_dd', 'value'),
     State('long_dd', 'value'),
     ]
)
def find_listings(n_clicks, lat_dd, long_dd):
    max_dist = 15 * n_clicks
    index_directory = []
    intersect, circle = find_intersecting_counties(lat_dd, long_dd, max_dist)
    for i in range(len(df)):
        if df.iloc[i]['county'] in intersect:
            index_directory.append(i)
    df_to_show = df.iloc[index_directory]
    figure = create_map( df_to_show, lat_dd, long_dd, circle)

    return figure
