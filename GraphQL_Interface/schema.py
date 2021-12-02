import graphene


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
    year = graphene.Int()
    manufacturer = graphene.String()
    condition = graphene.String()
    miles = graphene.Int()
    type = graphene.String()
    transmission = graphene.String()
    drive = graphene.String()
    color = graphene.String()

    @property
    def ltlng(self):
        return f"({self.lat},{self.lng})"


class VehicleCompare(graphene.ObjectType):
    ltlng = graphene.String()


class VehicleSearch(graphene.ObjectType):
    ltlng = graphene.String()


class Query(graphene.ObjectType):
    vehicle_compare = graphene.Field(VehicleCompare, geo=GeoInput(required=True))
    vehicle_search = graphene.Field(VehicleSearch, geo=GeoInput(required=True))

    def resolve_vehicle_compare(root, info, geo):
        return VehicleCompare(ltlng=geo.ltlng)
        # to be returned: a min, mean, and max value
        # given by supplied search_cat value

    def resolve_vehicle_search(root, info, geo):
        return VehicleSearch(ltlng=geo.ltlng)
        # to be returned: a list of car ids, to then be
        # prompted by another resolve function for specific
        # demanded details on each vehicle

# class CreateAddress(graphene.Mutation):
#     class Arguments:
#         geo = GeoInput(required=True)
#
#     Output = Address
#
#     def mutate(root, info, geo):
#         return Address(ltlng=geo.ltlng)


# class Mutation(graphene.ObjectType):
#     create_address = CreateAddress.Field()


schema = graphene.Schema(query=Query)
query = """
    query something{
      vehicleCompare(geo: {lat:32.2, lng:12}) {
        ltlng
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
