from os import error
from sys import audit
import discord 

import user_service as usr_serv
from event_service import new_event, update_event, get_location_by_event
import message_service as msg_serv
from resource import steps, msg_dict, error
from Event.event import Location
from GamePLanner import client 

async def building_together(message):
    authorDb = await usr_serv.get_or_create_user(message.author)
    event = event_serv.get_last_event_by_userId(authorDb.id)
    authorDb.print()
    event.print()
    print(f" this is the event i found from {authorDb.name} - {event.print()}")
    if event == None:
        await message.author.send(error['event-not-found'])
        return
    next_step(message, authorDb, event)

#Steps
async def next_step(message, authorDb, event):

    if event.step == steps['none']:
        new_event(message, authorDb)
        event.step = steps['game_name']
        await update_event(event)
        await message.author.send(msg_dict['game_name'])
    elif event.step == steps['init']:
        event.step = steps['game_name']
        await update_event(event)
        message.author.send(msg_dict['game_name'])

    elif event.step == steps['game_name']:
        event.gameName = message.content
        event.step = steps['slots']
        await update_event(event)
        message.author.send(msg_dict['slots'])

    elif event.step == steps['slots']:
        event.gameName = message.content
        event.step = steps['time']
        await update_event(event)
        message.author.send(msg_dict['time'])

    elif event.step == steps['time']:
        event.gameName = message.content
        event.step = steps['role']
        await update_event(event)
        message.author.send(msg_dict['role'])

    elif event.step == steps['role']:
        event.gameName = message.content
        event.step = steps['done']
        await update_event(event)
        message.author.send(msg_dict['done'])
        Location = get_location_by_event(event)
        channel = client.get_channel(int(Location.channelId))
        channel.send(await msg_serv.BuildInvitMessage(event, authorDb))

