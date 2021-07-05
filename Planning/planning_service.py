from os import error, name
from sys import audit
from discord import Color 
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button

from user_service import get_or_create_user
from event_service import new_event, update_event, get_location_by_event, get_last_event_by_userId, delete_event_from_authorId
import resources as res
import user_service as usr_service
import message_service as msg_serv
import game_service as game_serv
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
        game = await game_serv.known_game(message.content)
        event.game_id = game.id
        if game.image == "":
            event.step = res.steps['game_image']
            await message.author.send(res.msg_dict['game_image'])
        else:
            event.step = res.steps['slots']
            await message.author.send(res.msg_dict['slots'])
        await update_event(event)

    elif event.step == res.steps['game_image']:
        await game_serv.add_image(event.game_id, message.content)
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
        event.step = res.steps['done']
        await update_event(event)
        await message.author.send(res.msg_dict['done'])
        Location = await get_location_by_event(event)
        channel = bot.get_channel(int(Location.channelId))
        bot_message = await msg_serv.send_or_edit_event_message(channel, 
                                            event, authorDb, Color.gold(), 
                                            buttons_builder(['ok', 'late', 'cancel']),
                                            False)
        await buttons_management(bot_message, authorDb, event, bot)

async def  buttons_management(bot_message, authorDb, event, bot):
    while len(event.players) < event.slots:
        interaction = await bot.wait_for("button_click")
        userDb = await get_or_create_user(interaction.user)
        if interaction.component.label == res.button_text['ok']:
            if userDb.displayName in event.late:
                event.remove_late_player(userDb)
            await interaction.respond(content=res.msg_dict['added'])
            event.add_player(userDb)
            await update_event(event)
            await msg_serv.send_or_edit_event_message(bot_message, 
                                            event, authorDb, Color.gold(), 
                                            buttons_builder(['ok', 'late', 'cancel']),
                                            True)
        elif interaction.component.label == res.button_text['cancel']:
            if (authorDb.id == userDb.id):
                event.step = res.steps['cancel']
                await update_event(event)
                await interaction.respond(content=res.msg_dict["correctly cancel"])
                await msg_serv.send_or_edit_event_message(bot_message, event, authorDb, Color.red(), [], True)
                return
            else:
                if event.remove_player(userDb) == True:
                    await update_event(event)
                    await interaction.respond(content=res.msg_dict["correctly remove"])
                    await msg_serv.send_or_edit_event_message(bot_message, 
                        event, authorDb, Color.gold(), 
                        buttons_builder(['ok', 'late', 'cancel']),
                        True)
                else:
                    await interaction.respond(content=res.msg_dict["not on event"])
        elif interaction.component.label == res.button_text['late']:
            event.add_late_player(userDb)
            await update_event(event)
            await msg_serv.send_or_edit_event_message(bot_message, 
                event, authorDb, Color.gold(), 
                buttons_builder(['ok', 'late', 'cancel']),
                True
            )
            await interaction.respond(content=res.msg_dict['added'])

    await msg_serv.send_or_edit_event_message(bot_message, event, authorDb, Color.green(), [], True)

async def CancelCurrentEvent(message):
    authorDb = await get_or_create_user(message.author)

    value = await delete_event_from_authorId(authorDb.id)
    if value == None:
        await message.author.send(res.msg_dict['nothing_cancel'])
    else:
        await message.author.send(res.msg_dict['cancel'])

async def pass_event_image(message):
    author = await usr_service.get_by_discord_id(message.author.id)
    if author == None:
        await message.channel.send(res.error['not_next'])
        return None
    event = await get_last_event_by_userId(author.id)
    if event == None:
        await message.channel.send(res.error['not_next'])
        return None
    event.step = res.steps['slots']
    await update_event(event)
    await message.author.send(res.msg_dict['next'])
    await message.author.send(res.msg_dict['slots'])    


def buttons_builder(buttons_list):
    buttons = []

    for elem in buttons_list:
        style = res.button_style[elem]
        buttons.append(Button(disabled=0, label=res.button_text[elem], style = style, id=res.button_text[elem]))
    return buttons
