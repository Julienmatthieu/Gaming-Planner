import mysql.connector
from mysql.connector import Error
import keys

def get_connection():
    return mysql.connector.connect(host=keys.host,
                                         database=keys.database,
                                         user=keys.user,
                                         password=keys.password)

def close_connection(connection):
    if connection:
        connection.close()
