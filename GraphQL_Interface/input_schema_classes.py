import graphene
from GraphQL_Interface.sql_data_interface import search_function


class SearchCategory(graphene.Enum):
    RADIUS = 1
    REGIONAL = 2
    FLEX = 3
    STATS = 4


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

    def clean_data(self):
        """cleans data before sending it to vehicle retrieval function"""
        data = {'lat': self.lat, 'search_cat': self.search_cat, 'radius': self.radius,
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
    def search(self):
        data = self.clean_data()
        if data['search_cat'] != 'RADIUS' and data['search_cat'] != 'REGION' and data['search_cat'] != 'FLEX':
            return 'Error, search category provided not supported'
        print('check internal search cat: \n',
              self['search_cat'])
        final_return = search_function(data)
        return final_return
