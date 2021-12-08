import pandas as pd
from GraphQL_Interface.map_data.circle_intersection_functions import find_intersecting_counties
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dealers_cache = {}


def get_vehicle(id, data=None):
    """Simple function to return Vehicle from Database. Input vehicle id."""
    if data is not None:
        resp = data.to_dict()
    else:
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM vehicles WHERE id = {id}"""
            if 'limit' in data:
                query += f"""LIMIT {data['limit']}"""
                del data['limit']
            resp = pd.read_sql(query, cnx).iloc[0].to_dict()
        finally:
            cnx.close()

    return resp


def get_dealer(id, data=None):
    """simple function to return dealer. Input dealer ID."""
    if data is not None:
        resp = data.to_dict()
    else:
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM dealers WHERE id = '{id}'"""
            resp = pd.read_sql(query, cnx).iloc[0].to_dict()
            if data is not None:
                if 'limit' in data:
                    query += f"""LIMIT {data['limit']}"""
                    del data['limit']
        finally:
            cnx.close()

    return resp


def dealer_query(counties, data):
    """function for formatting query"""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query_p1 = """SELECT * FROM dealers WHERE"""
        query_p2 = """ county ="""
        for count in counties:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1[:-3]
        if 'limit' in data:
            query += f"""LIMIT {data['limit']}"""
            del data['limit']
        dealers = pd.read_sql(query, cnx)
    finally:
        cnx.close()
    return dealers


def vehicle_query(ids):
    """function for formatting query and return data from database"""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))

        query_p1 = """SELECT * FROM vehicles WHERE """
        query_p2 = """ dealer_ID ="""
        for count in ids['id'][:-1]:
            query_p1 += query_p2 + f""" '{count}' OR"""
        query = query_p1 + query_p2 + ' ' + "'" + str(ids['id'][len(ids) - 1]) + "'"
        data = pd.read_sql(query, cnx)
    finally:
        cnx.close()
    return data


def search_function(data):
    print('found search function')

    def option_1(long_dd, lat_dd, data):
        print('made it to the correct function block', data)
        """for basic radius search"""
        lat_adj = (lat_dd * 69)
        long_adj = (long_dd * 54.6)
        final_distance = data['radius']
        del data['radius']
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM dealers WHERE """ \
                    f"""(SQRT((((c1*69) - {lat_adj}) * ((c1*69) - {lat_adj}))""" \
                    f"""+ (((c2*54.6) - {long_adj})*((c2*54.6) - {long_adj}))) < {final_distance}); """
            ids = pd.read_sql(query, cnx)
            sql_return = vehicle_query(ids)
        finally:
            cnx.close()
        vehicle_lists = []
        for i in range(len(sql_return)):
            row = sql_return.iloc[i]
            vehicle_lists.append(get_vehicle(row['id'], row))
        return vehicle_lists

    def option_2(long_dd, lat_dd, data):
        """for regional search"""
        radius = data['radius']
        print('found option 2, :\n', data)
        del data['radius']
        intersect, circle = find_intersecting_counties(lat_dd, long_dd, radius)
        ids = dealer_query(intersect, data)
        sql_return = vehicle_query(ids)
        vehicle_lists = []
        for i in range(len(sql_return)):
            row = sql_return.iloc[i]
            vehicle_lists.append(get_vehicle(row['id'], row))
        return vehicle_lists

    long_dd = data['long']
    lat_dd = data['lat']
    search = data['search_cat']
    del data['long']
    del data['lat']
    del data['search_cat']
    if search == 'RADIUS':
        return option_1(long_dd, lat_dd, data)
    elif search == 'REGION':
        return option_2(long_dd, lat_dd, data)
    else:
        return 'not yet implemented'
