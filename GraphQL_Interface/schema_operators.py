import graphene
from GraphQL_Interface.schema_components import Vehicle, Dealer
from GraphQL_Interface.sql_data_interface import get_vehicle, get_dealer


class Query(graphene.ObjectType):
    vehicle = graphene.Field(Vehicle, id=graphene.Int(required=True))
    dealer = graphene.Field(Dealer, id=graphene.String(required=True))

    def resolve_vehicle(root, info, id):
        print('made it to the correct resolve')
        return get_vehicle(id)

    def resolve_dealer(root, info, id):
        return get_dealer(id)


schema = graphene.Schema(query=Query)

query = """
    query something {
      dealer(id: "DA2926"){
        name
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
