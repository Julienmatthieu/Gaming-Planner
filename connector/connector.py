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

def select_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    close_connection(connection)
    return records

def insert_query(query):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    records = cursor.fetchall()
    connection.commit()
    id = cursor.lastrowid
    close_connection(connection)
    return id
