from os import error
from sys import audit
import discord 


import user_service as usr_serv
import event_service as event_serv
import message_service as msg_serv
import resource as res
from Event.event import Location
from GamePLanner import client 

async def planning_event(message):
    authorDb = await usr_serv.get_or_create_user(message.author)
    event = event_serv.get_last_event_by_userId(authorDb.id)
    authorDb.print()
    event.print()
    print(f" this is the event i found from {authorDb.name} - {event.print()}")
    if event == None:
        await message.author.send(res.error['event-not-found'])
        return
    next_step(message, authorDb, event)

#Steps
async def next_step(message, authorDb, event):

    if event.step == res.steps['none']:
        event_serv.new_event(message, authorDb)
        event.step = res.steps['game_name']
        await event_serv.update_event(event)
        await message.author.send(res.msg_dict['game_name'])
    elif event.step == res.steps['init']:
        event.step = res.steps['game_name']
        await event_serv.update_event(event)
        message.author.send(res.msg_dict['game_name'])

    elif event.step == res.steps['game_name']:
        event.gameName = message.content
        event.step = res.steps['slots']
        await event_serv.update_event(event)
        message.author.send(res.msg_dict['slots'])

    elif event.step == res.steps['slots']:
        event.gameName = message.content
        event.step = res.steps['time']
        await event_serv.update_event(event)
        message.author.send(res.msg_dict['time'])

    elif event.step == res.steps['time']:
        event.gameName = message.content
        event.step = res.steps['role']
        await event_serv.update_event(event)
        message.author.send(res.msg_dict['role'])

    elif event.step == res.steps['role']:
        event.gameName = message.content
        event.step = res.steps['done']
        await event_serv.update_event(event)
        message.author.send(res.msg_dict['done'])
        Location = event_serv.get_location_by_event(event)
        channel = client.get_channel(int(Location.channelId))
        channel.send(await msg_serv.BuildInvitMessage(event, authorDb))

