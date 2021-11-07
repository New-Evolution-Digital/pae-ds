import dash_bootstrap_components as dbc
import dash
import os



external_stylesheets = [
    dbc.themes.UNITED, # Bootswatch theme
    'https://use.fontawesome.com/releases/v5.9.0/css/all.css', # for social media icons
]

meta_tags=[
    {'name': 'viewport', 'content': 'width=device-width, initial-scale=1'}
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)
server = app.server
app.config.suppress_callback_exceptions = True # see https://dash.plot.ly/urls

server.config.update(
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)
app.title = 'test auto app'