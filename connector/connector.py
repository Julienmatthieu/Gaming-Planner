import mysql.connector
from mysql.connector import Error
import ressources

def get_connection():
    return mysql.connector.connect(host=ressources.host,
                                         database=ressources.database,
                                         user=ressources.user,
                                         password=ressources.password)

def close_connection(connection):
    if connection:
        connection.close()
