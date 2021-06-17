import mysql.connector
from mysql.connector import Error
import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(f'{path}/connector/')
import event
import connector 

# Getters 
def get_event(event_id):
    records = connector.select_query(f"""SELECT * FROM event WHERE id = {event_id}""")
    row = records[0]
    current = event.build_event(row[0], row[1], row[2]) 
    return current

def get_all_event():
    list = []

    records = connector.select_query("""SELECT * FROM event""")
    for row in records:
        current = event.build_event(row[0], row[1], row[2]) 
        list.append(current)
    return list

def get_location(location):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE serverId = {location.serverId} AND channelId = {location.channelId} AND messageId = {location.messageId} """)
    row = records[0]
    current = event.build_location(row[0], row[1], row[2], row[3], row[4]) 
    return current

def get_eventid_by_location(location):
    location = get_location(location)
    return location.eventId

def get_location_by_event(eventId):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE eventId = {eventId} """)
    row = records[0]
    current = event.build_location(row[0], row[1], row[2], row[3], row[4]) 
    return current

def get_event_from_location(serverId, channelId, messageId):
    id = get_eventid_by_location(serverId, channelId, messageId)
    event = get_event(id)
    return event

def create_event(event, location):
    eventId = connector.insert_query(f"""INSERT INTO event (players, time) VALUES ("{event.players}", "{event.time}") """)
    locationId = connector.inset_query(f"""INSERT INTO discordLocation (serverId, channelId, messageId, eventId) VALUES ({location.serverId}, {location.channelId}, {location.messageId}, {eventId}) """)
    return eventId

def delete_event(id):
    connector.delete_query(f""" DELETE FROM discordLocation WHERE eventId = {id} """)
    connector.delete_query(f""" DELETE FROM event WHERE id = {id} """)
