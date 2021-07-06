import time
from location import Location 
import connector 
import resources as res

async def update_location_message(location):
    timestamp = time.strftime('%Y-%m-%d %H-%M-%S')

    query = f"""UPDATE discordLocation SET messageId = \"{location.messageId}\", on_update = \"{timestamp}\"  WHERE id = {location.id} """
    eventId = connector.alter_query(query)
    return eventId

async def create_location(location):
    query = f"""INSERT INTO discordLocation (guildId, channelId, messageId, eventId) VALUES (\"{location.guildId}\", \"{location.channelId}\", \"{location.messageId}\", {location.eventId}) """
    location.id = connector.alter_query(query)
    return location

async def get_location_by_guild_and_channel(guildId, channelId):
    records = connector.select_query(f"""SELECT * FROM discordLocation WHERE guildId = {guildId} AND channelId = {channelId} AND messageId = 0 ORDER BY eventId DESC""")
    if len(records) == 0:
        return None
    row = records[0]
    location = Location(row[0], row[1], row[2], row[3], row[4]) 
    return location 