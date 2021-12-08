import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

dealer_cache = {}
vehicle_cache = {}


def get_vehicle_from_dealer(id, limit=None):
    """Simple function to return Vehicle from Database. Input dealer id."""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query = f"""SELECT * FROM vehicles WHERE dealer_ID = '{id}'"""
        if limit is not None:
            query += f"""LIMIT {limit}"""
        resp = pd.read_sql(query, cnx)
        vehicle_lists = []
        for i in range(len(resp)):
            row = resp.iloc[i]
            vehicle_lists.append(row.to_dict())
    finally:
        cnx.close()
    return vehicle_lists


def get_dealer_from_vehicle(id):
    """simple function to return dealer. Input dealer ID."""
    try:
        cnx = mysql.connector.connect(user=os.getenv('USERNAME'), database=os.getenv('DATABASE'),
                                      port=os.getenv('PORT'),
                                      host=os.getenv('HOST'), password=os.getenv('PASSWORD'))
        query = f"""SELECT * FROM dealers WHERE id = '{id}'"""
        resp = pd.read_sql(query, cnx).iloc[0].to_dict()
    finally:
        cnx.close()
    return resp
