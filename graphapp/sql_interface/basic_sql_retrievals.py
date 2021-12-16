import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dealer_cache = {}
vehicle_cache = {}


def get_vehicle_from_dealer(id, limit=None):
    """Simple function to return Vehicle from Database. Input dealer id."""
    if id in vehicle_cache:
        vehicle_list = vehicle_cache[id]
    else:
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM vehicles WHERE dealer_ID = '{id}'"""
            if limit is not None:
                query += f"""LIMIT {limit}"""
            resp = pd.read_sql(query, cnx)
            vehicle_list = []
            for i in range(len(resp)):
                row = resp.iloc[i]
                vehicle_list.append(row.to_dict())
            vehicle_cache[id] = vehicle_list
        finally:
            cnx.close()
    return vehicle_list


def get_dealer_from_vehicle(id):
    """simple function to return dealer. Input dealer ID."""
    if id in dealer_cache:
        resp = dealer_cache[id]
    else:
        try:
            cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                          port=os.getenv('PORT'),
                                          host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
            query = f"""SELECT * FROM dealers WHERE id = '{id}'"""
            resp = pd.read_sql(query, cnx).iloc[0].to_dict()
            dealer_cache[id] = resp
        finally:
            cnx.close()
    return resp
