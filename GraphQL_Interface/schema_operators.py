import graphene
from GraphQL_Interface.sql_interface.sql_data_interface import get_vehicle, get_dealer
from GraphQL_Interface.sql_interface.basic_sql_retrievals import get_dealer_from_vehicle, get_vehicle_from_dealer
from GraphQL_Interface.sql_interface.sql_data_interface import search_function


class SearchInput(graphene.InputObjectType):
    search_cat = graphene.String(default_value='REGIONAL')
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
    limit = graphene.Int(default_value=None)

    def clean_data(self):
        """cleans data before sending it to vehicle retrieval function"""
        data = {'lat': self.lat, 'search_cat': self.search_cat, 'radius': self.radius,
                'long': self.lng, 'year': self.year, 'manufacturer': self.manufacturer,
                'model': self.model, 'condition': self.condition, 'odometer': self.miles,
                'type': self.type, 'transmission': self.transmission, 'drive': self.drive,
                'color': self.color, 'limit': self.limit}
        to_del = []
        for key, value in data.items():
            if value is None:
                to_del.append(key)
        for key in to_del:
            del data[key]
        return data

    @property
    def search(self):
        data = self.clean_data()
        if data['search_cat'] != 'RADIUS' and data['search_cat'] != 'REGION' and data['search_cat'] != 'FLEX':
            return 'Error, search category provided not supported'
        print('check internal search cat: \n',
              self['search_cat'])
        return [vehicle_objectify(x) for x in search_function(data)]


class Vehicle(graphene.ObjectType):
    id = graphene.ID(required=True)
    year = graphene.Int()
    manufacturer = graphene.String()
    model = graphene.String()
    condition = graphene.String()
    odometer = graphene.Int()
    type = graphene.String()
    transmission = graphene.String()
    drive = graphene.String()
    color = graphene.String()
    price = graphene.Int()
    cylinders = graphene.String()
    VIN = graphene.String()
    dealer = graphene.ID()
    dealer_retrieval = graphene.List(lambda: Dealer)

    def resolve_dealer_retrieval(self, info):
        return [dealer_objectify(get_dealer_from_vehicle(self.dealer))]


class Dealer(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    city = graphene.String()
    limit = graphene.Int()
    vehicles = graphene.List(lambda: Vehicle)

    def resolve_vehicles(self, info):
        return [vehicle_objectify(x) for x in get_vehicle_from_dealer(self['id'])]


def vehicle_objectify(resp):
    """returns vehicle object from input"""
    vehicle_object = Vehicle(
        id=resp['id'],
        year=resp['year'],
        manufacturer=resp['manufacturer'],
        model=resp['model'],
        condition=resp['cond'],
        odometer=resp['odometer'],
        type=resp['type'],
        transmission=resp['transmission'],
        drive=resp['drive'],
        color=resp['paint_color'],
        price=resp['price'],
        cylinders=resp['cylinders'],
        VIN=resp['VIN'],
        dealer=resp['dealer_ID']
    )
    return vehicle_object

def dealer_objectify(resp):
    dealer_object = Dealer(
        id=resp['id'],
        city=resp['city'],
        name=resp['name']
    )
    return dealer_object


class VehicleSearch(graphene.ObjectType):
    searchResult = graphene.List(lambda: Vehicle)


class Query(graphene.ObjectType):
    vehicle_lookup = graphene.Field(Vehicle, id=graphene.Int(required=True))
    dealer_lookup = graphene.Field(Dealer, id=graphene.String(required=True))
    vehicle_search = graphene.Field(VehicleSearch, submission=SearchInput(required=True))

    def resolve_vehicle_lookup(root, info, id):
        return get_vehicle(id)

    def resolve_dealer_lookup(root, info, id):
        return get_dealer(id)

    def resolve_vehicle_search(root, info, submission):
        return VehicleSearch(searchResult=submission.search)


schema = graphene.Schema(query=Query)

query = """
    query something {
      dealerLookup(id: "DA2926"){
        name
        vehicles {
            model
            dealerRetrieval {
                name
              }
          }
      }
    }
"""

query2 = """
    query something {
      vehicleSearch(submission: {lat:43.95, lng:-120.54, manufacturer: "toyota", searchCat: "REGION"}) {
        searchResult {
          model
          manufacturer
          condition          
        }
      }
    }
"""


def test_query():
    result = schema.execute(query)
    assert not result.errors
    assert result.data == {"vehicleCompare": {"latlng": "(32.2,12.0)"}}


if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data)
