import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


from app import app, server
from pages import map_here, county_search

navbar = dbc.NavbarSimple(
    brand='Listing Return',
    brand_href='/',
    children=[
        dbc.NavItem(dcc.Link('Basic', href='/', className='nav-link')),
        dbc.NavItem(dcc.Link('Regional/Zip', href='/zip', className='nav-link')),
    ],
    sticky='top',
    color='light',
    light=True,
    dark=False
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(),
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return map_here.layout
    elif pathname == '/zip':
        return county_search.layout


if __name__ == '__main__':
    app.run_server(debug=True)