import graphene
import requests
import os

URL = os.getenv('URL')
SECRET = os.getenv('SECRET_TOKEN')


class vehicleData(graphene.InputObjectType):
    longitude = graphene.Float()
    latitude = graphene.Float()
    year = graphene.Int()
    manufacturer = graphene.String()
    condition = graphene.String()
    miles = graphene.Int()
    type = graphene.String()
    transmission = graphene.String()
    drive = graphene.String()
    color = graphene.String()
    fuel = graphene.String()


class Radius(graphene.ObjectType):
    radius = graphene.Int(required=True)

class Option(graphene.Enum):
    option = graphene.String()


class Query(graphene.ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    vehicleStats = graphene.Field(vehicle=vehicleData(required=True))
    vehicleListings = graphene.Field(Option, Radius, vehicle=vehicleData())

    def resolve_vehicleStats(root, info, vehicle):
        resp = requests.post(URL + '/vehicledata/metrics', auth=SECRET,
                             data=vehicle)
        return resp

    def resolve_vehicleListings(root, info, vehicle):
        resp = requests.post(URL + 'vehicledata/listings', auth=SECRET,
                             data=vehicle)
        return resp


schema = graphene.Schema(query=Query, types=[vehicleData, Radius, Option])

# we can query for our field (with the default argument)
query_string = '{ goodbye }'
result = schema.execute(query_string)
print(result.data['goodbye'])
# "Hello stranger!"

# or passing the argument in the query
query_with_argument = '{ hello(name: "GraphQL") }'
result = schema.execute(query_with_argument)
print(result.data['hello'])
# "Hello GraphQL!"
