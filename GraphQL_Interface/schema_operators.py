import graphene
from GraphQL_Interface.schema_components import Vehicle, Dealer, VehicleSearch
from GraphQL_Interface.sql_data_interface import get_vehicle, get_dealer
from GraphQL_Interface.input_schema_classes import SearchInput


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
    result = schema.execute(query2)
    print(result.data)
