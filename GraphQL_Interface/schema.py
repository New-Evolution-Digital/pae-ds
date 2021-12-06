import graphene
from GraphQL_Interface.functions.vehicle_retrieval import regional_search, search_function


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
    search_cat = graphene.Int(default_value=None)
    radius = graphene.Int(default_value=30)
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

    def clean_data(self):
        """cleans data before sending it to vehicle retrieval function"""
        data = {'lat': self.lat, 'search-cat': self.search_cat, 'radius': self.radius,
                'long': self.lng, 'year': self.year, 'manufacturer': self.manufacturer,
                'model': self.model, 'condition': self.condition, 'odometer': self.miles,
                'type': self.type, 'transmission': self.transmission, 'drive': self.drive,
                'color': self.color}
        to_del = []
        for key, value in data.items():
            if value is None:
                to_del.append(key)
        for key in to_del:
            del data[key]
        return data

    @property
    def minmax(self):
        data = self.clean_data()
        final_return = regional_search(data)
        return str(final_return)

    @property
    def search(self):
        data = self.clean_data()
        print('check internal search cat: \n',
              self['search_cat'])
        final_return = regional_search(data, search=self['search_cat'])
        return final_return


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


class VehicleStats(graphene.ObjectType):
    minmax = graphene.String()


class BasicRadiusSearch(graphene.ObjectType):
    search = graphene.List(graphene.String)


class RegionalSearch(graphene.ObjectType):
    search = graphene.List(graphene.String)


class Query(graphene.ObjectType):
    vehicle_stats = graphene.Field(VehicleStats, geo=GeoInput(required=True))
    basic_radius_search = graphene.Field(BasicRadiusSearch, geo=GeoInput(required=True))
    regional_search = graphene.Field(RegionalSearch, geo=GeoInput(required=True))

    vehicle_id = graphene.Field(VehicleId)

    def resolve_vehicle_stats(root, info, geo):
        return VehicleStats(minmax=geo.minmax)
        # to be returned: a min, mean, and max value
        # given by supplied search_cat value

    def resolve_basic_radius_search(root, info, geo):
        geo['search_cat'] = 1
        return BasicRadiusSearch(search=geo.search)
        # to be returned: a list of car ids, to then be
        # prompted by another resolve function for specific
        # demanded details on each vehicle

    def resolve_regional_search(root, info, geo):
        pass
        return

    def resolve_vehicle_id(root, info, data):
        return VehicleId(year=1)


schema = graphene.Schema(query=Query)
query = """
    query something{
      vehicleStats(geo: {lat:43.95, lng:-120.54, manufacturer: "toyota"}) {
        minmax
      }
    }
"""

query2 = """
    query something{
      basicRadiusSearch(geo: {lat:43.95, lng:-120.54, manufacturer: "toyota", radius: 30}) {
        search
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
    result = schema.execute(query2)
    print(result.data)
