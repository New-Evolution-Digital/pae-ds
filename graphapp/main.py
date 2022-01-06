# flask_sqlalchemy/app.py
from flask import Flask
from graphql_server.flask import GraphQLView
from schema_operators import schema
import os
import mysql.connector
from dotenv import load_dotenv
import uvicorn

app = Flask(__name__)
app.debug = True
load_dotenv()

def index():
    cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                  port=os.getenv('PORT_NUMBER'),
                                  host=os.getenv('HOST'),
                                  password=os.getenv('PASSWORD'),
                                  ssl_ca=os.getenv('SSL'))
    curs = cnx.cursor()
    query = f"""SELECT * FROM dealers LIMIT 10"""
    curs.execute(query)
    alpha = curs.fetchall()
    return str(alpha)

app.view_functions['index'] = index

app.add_url_rule(
    '/',
    'index',
    index
)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.graphql_schema,
        graphiql=True # for having the GraphiQL interface
    )
)