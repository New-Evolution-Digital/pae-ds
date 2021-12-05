import graphene
from GraphQL_Interface.functions.vehicle_retrieval import regional_search


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
    def minmax(self):
        data = {'lat': self.lat,
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
        final_return = regional_search(data)
        return str(final_return)

    @property
    def search(self):
        data = {'lat': self.lat,
                'long': self.lng, 'year': self.year, 'manufacturer': self.manufacturer,
                'model': self.model, 'condition': self.condition, 'odometer': self.miles,
                'type': self.type, 'transmission': self.transmission, 'drive': self.drive,
                'color': self.color}
        pass
        return


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
    minMax = graphene.String()


class VehicleSearch(graphene.ObjectType):
    minMax = graphene.String()


class Query(graphene.ObjectType):
    print('made it through to the correct query')
    vehicle_stats = graphene.Field(VehicleStats, geo=GeoInput(required=True))
    vehicle_search = graphene.Field(VehicleSearch, geo=GeoInput(required=True))
    vehicle_id = graphene.Field(VehicleId)

    def resolve_vehicle_stats(root, info, geo):
        return VehicleStats(ltlng=geo.minmax)
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
      VehicleStats(geo: {lat:43.95, lng:-120.54, manufacturer: "toyota"}) {
        minMax
      }
    }
"""



def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {"vehicleCompare": {'min': 100, 'avg': 21601.936941493845, 'max': 299991}}


if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data)
