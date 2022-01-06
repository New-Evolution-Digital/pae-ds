import graphene
from sql_interface.sql_data_interface import get_vehicle, get_dealer
from sql_interface.basic_sql_retrievals import get_dealer_from_vehicle, get_vehicle_from_dealer
from sql_interface.sql_data_interface import search_function


class SearchCat(graphene.Enum):
    REGION = 1
    RADIUS = 2
    FLEX = 3

    @property
    def description(self):
        if self == SearchCat.REGION:
            return 'Regional Search method; finds all counties within a certain radial distance,' \
                   'then searches those counties for vehicles matchcing the provided features'
        elif self == SearchCat.RADIUS:
            return 'Radial search method; finds all vehicles matching feature description provided within' \
                   'the provided distance'
        else:
            return 'Flex Search method; finds all vehicles matching feature description provided within' \
                   'the provided distance. Additionally, provides vehicles outside of provided radial distance' \
                   'if the car is inexpensive enough to warrant the additional distance.'


class SearchInput(graphene.InputObjectType):
    search_cat = SearchCat(required=True)
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
        data['search_cat'] = self.search_cat.name
        final_return = search_function(data)
        return final_return


class Dealer(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    city = graphene.String()
    limit = graphene.Int()
    vehicles = graphene.List(lambda: Vehicle)

    def resolve_vehicles(self, info):
        return [vehicle_objectify(x) for x in get_vehicle_from_dealer(self['id'])]


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
    dealer_id = graphene.ID()
    dealer = graphene.Field(Dealer)

    def resolve_dealer(self, info):
        return dealer_objectify(get_dealer_from_vehicle(self.dealer_id))


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
        dealer_id=resp['dealer_ID']
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
            dealer {
                name
              }
          }
      }
    }
"""
#mysql -h mysql–instance1.123456789012.us-east-1.rds.amazonaws.com --ssl-ca=global-bundle.pem -P 3306 -u mymasteruser -p
query2 = """
    query something {
      vehicleSearch(submission: {lat:43.95, lng:-120.54, manufacturer: "toyota" searchCat: RADIUS}) {
        searchResult {
          model
          manufacturer
          condition          
        }
      }
    }
"""

if __name__ == "__main__":
    result = schema.execute(query)
    print(result.data)
