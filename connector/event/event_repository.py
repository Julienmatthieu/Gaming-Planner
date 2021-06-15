import mysql.connector
from mysql.connector import Error
import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(f'{path}/connector/')
import event
import connector 

def get_event(event_id):
    records = connector.select_query(f"""select * from event where id = {event_id}""")
    row = records[0]
    current = event.make_event(row[0], row[1], row[2]) 
    return current

def get_all_event():
    list = []

    records = connector.select_query("""select * from event""")
    for row in records:
        current = event.make_event(row[0], row[1], row[2]) 
        list.append(current)
    return list

    #connection = connector.get_connection()
    #cursor = connection.cursor()
    #select_query = 
    #cursor.execute(select_query)
    #records = cursor.fetchall()
    #for row in records:
    #    current = event.make_event(row[0], row[1], row[2]) 
    #    list.append(current)
    #connector.close_connection(connection)
    #return list

def get_event_from_location(serverId, channelId, messageId):
    connection = connector.get_connection()
    cursor = connection.cursor()
    select_query = f"""select eventId from discordLocation where serverId = {serverId} AND channelId = {channelId} AND messageId = {messageId} """
    cursor.execute(select_query)
    records = cursor.fetchall()
    event = get_event(records[0][0])
    connector.close_connection(connection)
    return event

def create_event():
    connection = connector.get_connection()
    cursor = connection.cursor()
    select_query = f"""INSERT INTO event (players, time) VALUES ("juju, steve", "asap") """
    cursor.execute(select_query)
    connection.commit()
    records = cursor.fetchall()
    print(f"this is my creation query: {records}")
    connector.close_connection(connection)
    return event