import time
from event import Event 
from location import Location
import location_service as loc_serv
import resources as res
import connector 

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
    event.id = connector.alter_query(query)
    location.eventId = event.id
    location = await loc_serv.create_new_location(location)
    return event

async def get_event(event_id):
    records = connector.select_query(f"""SELECT * FROM event WHERE id = {event_id}""")
    row = records[0]
    current = Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 
    return current 

# update 

async def update_event(event):

    timestamp = time.strftime('%Y-%m-%d %H-%M-%S')
    query = f"""UPDATE event SET players = \"{stringify_to_db(event.players)}\", time = \"{event.time}\", slots = \"{event.slots}\", \
                                authorId = \"{event.authorId}\", role = \"{event.role}\", step = \"{event.step}", players_id = \"{stringify_to_db(event.players_id)}\", \
                                game_id = \"{event.game_id}\", late = \"{stringify_to_db(event.late)}\", on_update = \"{timestamp}\" \
                                WHERE id = {event.id} """
    connector.alter_query(query)
    return event   

# Getters 

async def get_by_userId(userId):
    query = f""" SELECT * FROM event WHERE step >= {res.steps['init']}  AND authorId = {userId} ORDER BY id desc """
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    return Event(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]) 

async def get_location(location):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE guildId = {location.guildId} AND channelId = {location.channelId} AND messageId = {location.messageId} """)
    row = records[0]
    location = Location(row[0], row[1], row[2], row[3], row[4]) 
    return location

async def get_eventid_by_location(location):
    location = await get_location(location)
    return location.eventId

async def get_event_from_location(guildId, channelId, messageId):
    id = get_eventid_by_location(guildId, channelId, messageId)
    event = await get_event(id)
    return event

async def delete_event(id):
    connector.delete_query(f""" DELETE FROM discordLocation WHERE eventId = {id} """)
    connector.delete_query(f""" DELETE FROM event WHERE id = {id} """)
