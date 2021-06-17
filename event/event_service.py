import discord 

import event_repository as repo
from event import Event, Location
import ressources as res

async def get_last_unset_event(message):
    location = await repo.get_last_location(message.guild.id, message.channel.id)
    if (location == None):
        return
    location.messageId = message.id
    await repo.update_location_message(location)
    return await repo.get_event(location.eventId)

async def new_event(message, author):
    print("\n\n --------------- 1 ---------------\n\n")
    
    new_event = Event(id=0, player=message.author.name, time="", slots=1, gameName="", authorId=author.id, role="", step=res.steps['init'])
    print("\n\n --------------- 2 ---------------\n\n")
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    print("\n\n --------------- 3 ---------------\n\n")
    return await repo.create_event(new_event, new_location)

async def update_event(content, author, event):
    data=content.split('-')
    new_event = Event(id=0, gameName=data[1], slots=int(data[2]), time=data[3], authorId=author.id, player=author.name, role=data[4], step=res.steps['done'])
    event.merge(new_event)
    return await repo.update_event(event)