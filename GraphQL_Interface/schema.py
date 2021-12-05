import graphene
from GraphQL_Interface.functions.vehicle_retrieval import regional_search


class SearchType(graphene.Enum):
    REGION_SEARCH = 1
    BASIC_SEARCH = 2
    FLEX_SEARCH = 3

    @property
    def description(self):
        if self == SearchType.REGION_SEARCH:
            return 'regional Search'
        elif self == SearchType.BASIC_SEARCH:
            return 'basic, radius search'
        else:
            return 'flex search'


class GeoInput(graphene.InputObjectType):
    search_cat = SearchType(default_value=1)
    lat = graphene.Float(required=True)
    lng = graphene.Float(required=True)
    year = graphene.Int(default_value=None)
    manufacturer = graphene.String(default_value=None)
    model = graphene.String(default_value=None)
    condition = graphene.String(default_value=None)
    miles = graphene.Int(default_value=None)
    type = graphene.String(default_value=None)
    transmission = graphene.String(default_value=None)
    drive = graphene.String(default_value=None)
    color = graphene.String(default_value=None)

    @property
    def ltlng(self):
        print('latlng called properly from geo input class')
        data = {'lat': self.lat,
                'long': self.lng, 'year': self.year, 'manufacturer': self.manufacturer,
                'model': self.model, 'condition': self.condition, 'odometer': self.miles,
                'type': self.type, 'transmission': self.transmission, 'drive': self.drive,
                'color': self.color}
        print(data, '\nabove data in place')
        to_del = []
        for key, value in data.items():
            if value is None:
                to_del.append(key)
        print(to_del, '\n above array to be deleted from data input')
        for key in to_del:
            del data[key]
        print(data, 'resulting data set')
        final_return = regional_search(data)
        print(final_return, 'return from function')
        return str(final_return)


class VehicleId(graphene.ObjectType):
    year = graphene.Int()
    manufacturer = graphene.String()
    model = graphene.String()
    condition = graphene.String()
    miles = graphene.Int()
    type = graphene.String()
    transmission = graphene.String()
    drive = graphene.String()
    color = graphene.String()


class VehicleCompare(graphene.ObjectType):
    ltlng = graphene.String()


class VehicleSearch(graphene.ObjectType):
    ltlng = graphene.String()


class Query(graphene.ObjectType):
    print('made it through to the correct query')
    vehicle_compare = graphene.Field(VehicleCompare, geo=GeoInput(required=True))
    vehicle_search = graphene.Field(VehicleSearch, geo=GeoInput(required=True))
    vehicle_id = graphene.Field(VehicleId)

    def resolve_vehicle_compare(root, info, geo):
        return VehicleCompare(ltlng=geo.ltlng)
        # to be returned: a min, mean, and max value
        # given by supplied search_cat value

    def resolve_vehicle_search(root, info, geo):
        return VehicleSearch(ltlng=geo.ltlng)
        # to be returned: a list of car ids, to then be
        # prompted by another resolve function for specific
        # demanded details on each vehicle

    def resolve_vehicle_id(root, info, data):
        return VehicleId(year=1)



schema = graphene.Schema(query=Query)
query = """
    query something{
      vehicleCompare(geo: {lat:43.95, lng:-120.54, manufacturer: "toyota"}) {
        minMax
      }
    }
"""
mutation = """
    mutation addAddress{
      createAddress(geo: {lat:32.2, lng:12}) {
        ltlng
      }
    }
"""


def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {"vehicleCompare": {"latlng": "(32.2,12.0)"}}


def test_mutation():
    result = schema.execute(mutation)
    assert not result.errors
    assert result.data == {"createAddress": {"latlng": "(32.2,12.0)"}}


if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data)
