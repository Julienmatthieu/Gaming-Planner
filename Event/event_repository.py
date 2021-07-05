import time
from event import Event, Location 
import connector 
import resources as res
import datetime

def stringify_to_db(list):
    if list == "":
        return "NULL"
    string = ""
    for elem in list:
        if string != "":
            string += res.databaseSeparator
        string += str(elem)
    return string

async def create_event(event, location):
    game_id = event.game_id
    if event.game_id == 0:
        game_id = "NULL"

    query = f"""INSERT INTO event (players, time, slots, authorId, role, step, players_id, game_id, late) VALUES \
            (\"{stringify_to_db(event.players)}\", \"{event.time}\", {event.slots}, \
            {event.authorId}, \"{event.role}\", {event.step}, \"{stringify_to_db(event.players_id)}\", {game_id}, \"{stringify_to_db(event.late)}\")  """
    eventId = connector.alter_query(query)
    query = f"""INSERT INTO discordLocation (guildId, channelId, messageId, eventId) VALUES (\"{location.guildId}\", \"{location.channelId}\", \"{location.messageId}\", {eventId}) """
    locationId = connector.alter_query(query)
    event.id = eventId
    return event

async def get_last_location(guildId, channelId):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE guildId = {guildId} AND channelId = {channelId} AND messageId = 0 ORDER BY eventId DESC""")
    if len(records) == 0:
        return None
    row = records[0]
    location = Location(row[0], row[1], row[2], row[3], row[4]) 
    return location 

async def get_event(event_id):
    records = connector.select_query(f"""SELECT * FROM event WHERE id = {event_id}""")
    row = records[0]
    current = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 
    return current 

# update 

async def update_event(event):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = f"""UPDATE event SET players = \"{stringify_to_db(event.players)}\", time = \"{event.time}\", slots = \"{event.slots}\", \
                                authorId = \"{event.authorId}\", role = \"{event.role}\", step = \"{event.step}", players_id = \"{stringify_to_db(event.players_id)}\", \
                                game_id = \"{event.game_id}\", late = \"{stringify_to_db(event.late)}\", on_update = \"{timestamp}\" \
                                WHERE id = {event.id} """
    connector.alter_query(query)
    return event   

async def update_location_message(location):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    query = f"""UPDATE discordLocation SET messageId = \"{location.messageId}\", on_update = \"{timestamp}\"  WHERE id = {location.id} """
    eventId = connector.alter_query(query)
    return eventId

# Getters 

async def get_by_userId(userId):
    query = f""" SELECT * FROM event WHERE step >= {res.steps['init']}  AND authorId = {userId} ORDER BY id desc """
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    return Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 

async def get_location_by_event(event):
    query = f""" SELECT * FROM discordLocation WHERE eventId = {event.id} """
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    return Location(row[0], row[1], row[2], row[3], row[4]) 

async def get_location(location):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE guildId = {location.guildId} AND channelId = {location.channelId} AND messageId = {location.messageId} """)
    row = records[0]
    location = Location(row[0], row[1], row[2], row[3], row[4]) 
    return location

async def get_eventid_by_location(location):
    location = await get_location(location)
    return location.eventId

async def get_location_by_event(event):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE eventId = {event.id} """)
    row = records[0]
    return Location(row[0], row[1], row[2], row[3], row[4]) 

async def get_event_from_location(guildId, channelId, messageId):
    id = get_eventid_by_location(guildId, channelId, messageId)
    event = await get_event(id)
    return event

async def delete_event(id):
    connector.delete_query(f""" DELETE FROM discordLocation WHERE eventId = {id} """)
    connector.delete_query(f""" DELETE FROM event WHERE id = {id} """)
