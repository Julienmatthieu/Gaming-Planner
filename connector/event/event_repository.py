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

def get_location(serverId, channelId, messageId):
    records = connector.select_query(f"""select eventId from discordLocation where serverId = {serverId} AND channelId = {channelId} AND messageId = {messageId} """)
    return records[0][0]

def get_event_from_location(serverId, channelId, messageId):
    location = get_location(serverId, channelId, messageId)
    event = get_event(location[0][0])
    return event

def create_event():
    id = connector.insert_query(f"""INSERT INTO event (players, time) VALUES ("juju, steve", "asap") """)
    print(f"this is my creation query: {id}")
    return None