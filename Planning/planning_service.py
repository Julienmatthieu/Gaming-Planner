from os import error, name
from sys import audit
from discord import Color 
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button

from user_service import get_or_create_user
from event_service import new_event, update_event, get_location_by_event, get_last_event_by_userId, delete_event_from_authorId
import resources as res
import message_service as msg_serv
from event import Event, Location

async def building_together(message, bot):
    
    authorDb = await get_or_create_user(message.author)
    event = await get_last_event_by_userId(authorDb.id)
    if event == None:
        await message.author.send(res.error['event-not-found'])
        return
    await next_step(message, authorDb, event, bot)

#Steps
async def next_step(message, authorDb, event, bot):
    ctx = await bot.get_context(message)
    if event.step == res.steps['none']:
        new_event(message, authorDb)
        event.step = res.steps['game_name']
        await update_event(event)
        await message.author.send(res.msg_dict['game_name'])
        
    elif event.step == res.steps['init']:
        event.step = res.steps['game_name']
        await update_event(event)
        await message.author.send(res.msg_dict['game_name'])

    elif event.step == res.steps['game_name']:
        event.gameName = message.content
        event.step = res.steps['slots']
        await update_event(event)
        await message.author.send(res.msg_dict['slots'])

    elif event.step == res.steps['slots']:
        event.slots = int(message.content)
        event.step = res.steps['time']
        await update_event(event)
        await message.author.send(res.msg_dict['time'])

    elif event.step == res.steps['time']:
        event.time = message.content
        event.step = res.steps['role']
        await update_event(event)
        await message.author.send(res.msg_dict['role'])

    elif event.step == res.steps['role']:
        event.role = message.content
        event.step = res.steps['done']
        await update_event(event)
        await message.author.send(res.msg_dict['done'])
        Location = await get_location_by_event(event)
        channel = bot.get_channel(int(Location.channelId))
        bot_message = await msg_serv.send_or_edit_event_message(channel, 
                                            event, authorDb, Color.gold(), 
                                            [
                                                Button(disabled=0, label=res.button['ok'], style = 3, id=res.button['ok']),
                                                Button(disabled=0, label=res.button['cancel'], style = 4, id=res.button['cancel'])
                                            ], 
                                            False)
        await buttons_management(bot_message, authorDb, event, bot)

async def  buttons_management(bot_message, authorDb, event, bot):
    ppl = 1 #event get_list_players TO DO
    while ppl < event.slots:
        interaction = await bot.wait_for("button_click")

        if interaction.component.label == res.button['ok']:
            await interaction.respond(content=res.msg_dict['added'])
            ppl += 1
        else:
            await interaction.respond(content="correctly cancel")
            await msg_serv.send_or_edit_event_message(bot_message, event, authorDb, Color.red(), [], True)
            return
    await msg_serv.send_or_edit_event_message(bot_message, event, authorDb, Color.green(), [], True)

async def CancelCurrentEvent(message):
    authorDb = await get_or_create_user(message.author)

    value = await delete_event_from_authorId(authorDb.id)
    if value == None:
        await message.author.send(res.msg_dict['nothing_cancel'])
    else:
        await message.author.send(res.msg_dict['cancel'])
