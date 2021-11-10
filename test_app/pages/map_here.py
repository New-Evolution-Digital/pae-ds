from dash import dcc
from dash import html
import numpy as np
import pandas as pd
from data.data_tools.generate_testing_dataset import df
from dash.dependencies import Input, Output, State
from test_app.mapping_funcs_and_data.map_functions import create_map
from app import app


#df = pd.read_csv('modified_csv')
center_lat = df['lat'].sum() / len(df)
center_long = df['lon'].sum() / len(df)
print(center_lat)
print(center_long)

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
            html.Iframe(id='MapPlot', srcDoc=create_map(None, center_lat, center_long, 0), width='100%', height=600)
        ])
    ]),
    html.Div(className='row', children=[
        html.Button('Fetch Cars', id='submit-val2', n_clicks=0)
    ])
]
)


@app.callback(
    Output('MapPlot', 'srcDoc'),
    [Input('submit-val2', 'n_clicks'),
     State('lat_dd', 'value'),
     State('long_dd', 'value'),
     ]
)
def find_listings(n_clicks, lat_dd, long_dd):
    to_show = []
    max_dist = 15 * n_clicks
    for i in range(len(df)):
        alpha = np.sqrt(
            ((df.iloc[i]['lat'] * 69) - (lat_dd * 69)) ** 2 + ((df.iloc[i]['long'] * 54.6) - (long_dd * 54.6)) ** 2)
        if not alpha > max_dist:
            to_show.append(i)
    df_to_show = df.iloc[to_show]
    figure = create_map(df_to_show, lat_dd, long_dd, max_dist)
    return figure
