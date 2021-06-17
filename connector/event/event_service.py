import discord 

import event_repository as repo
from event import Event, Location

async def get_last_unset_event(message):
    location = await repo.get_last_location(message.guild.id, message.channel.id)
    if (location == None):
        return
    location.messageId = message.id
    await repo.update_location_message(location)
    return await repo.get_event(location.eventId)

async def new_event(message, author):
    new_event = Event(id=0, player=message.author.name, time="", slots=1, gameName="", author=author.id, role="", step=res.steps['init'])
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    await repo.create_event(new_event, new_location)