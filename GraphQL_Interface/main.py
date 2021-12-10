# flask_sqlalchemy/app.py
from flask import Flask
from graphql_server.flask import GraphQLView
from GraphQL_Interface.schema_operators import schema

app = Flask(__name__)
app.debug = True

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema.graphql_schema,
        graphiql=True # for having the GraphiQL interface
    )
)

if __name__ == '__main__':
    app.run()