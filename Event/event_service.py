import discord 

import event_repository as repo
from event import Event, Location
import resources as res

async def get_last_unset_event(message):
    location = await repo.get_last_location(message.guild.id, message.channel.id)
    if (location == None):
        return
    location.messageId = message.id
    await repo.update_location_message(location)
    return await repo.get_event(location.eventId)

async def new_event(message, author):
    new_event = Event(id=0, players=message.author.display_name, time="", slots=1, gameName="", authorId=author.id, role="", step=res.steps['init'], players_id=message.author.id)
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    return await repo.create_event(new_event, new_location)

async def no_step(content, author, event):
    data=content.split('-')
    new_event = Event(id=0, gameName=data[1], slots=int(data[2]), time=data[3], authorId=author.id, players=author.display_name, role=data[4], step=res.steps['done'], players_id=author.id)
    event.merge(new_event)
    return await repo.update_event(event)

async def update_event(event):
    return await repo.update_event(event)

async def get_last_event_by_userId(userId):
    return await repo.get_by_userId(userId)

async def get_location_by_event(event):
    return await repo.get_location_by_event(event)
    
async def delete_event_from_authorId(authorId):
    event = await get_last_event_by_userId(authorId)

    if event == None:
        return
    await repo.delete_event(event.id)

async def get_by_id(id):
    return await repo.get_event(id)