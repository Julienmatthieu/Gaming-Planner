from time import process_time
import discord 

import event_repository as repo
import location_service as loc_serv
from event import Event
from location import Location

import resources as res

async def new_event(message, author):
    new_event = Event(id=0, players=message.author.name, 
                        time="", slots=1, authorId=str(author.id), 
                        role="", step=res.steps['init'], players_id=str(message.author.id), 
                        game_id=0, late=None)
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    return await repo.create_event(new_event, new_location)

async def update_event(event):
    return await repo.update_event(event)

async def get_last_event_by_userId(userId):
    return await repo.get_by_userId(userId)
   
async def delete_event_from_authorId(authorId):
    event = await get_last_event_by_userId(authorId)

    if event == None:
        return None
    await repo.delete_event(event.id)

async def get_by_id(id):
    return await repo.get_event(id)