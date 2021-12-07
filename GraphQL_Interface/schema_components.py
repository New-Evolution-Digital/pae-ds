import graphene


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


class Dealer(graphene.ObjectType):
    id = graphene.ID(required=True)
    name = graphene.String()
    city = graphene.String()


class SearchCategory(graphene.Enum):
    RADIUS = 1
    REGIONAL = 2
    FLEX = 3
    STATS = 4
