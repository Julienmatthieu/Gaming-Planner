#from os import name
import sys
import pathlib
from discord import Color
from discord.ext.commands import Bot
from discord_components import *
import time

path = pathlib.Path().absolute()
sys.path.append(f'{path}/Resources/')
sys.path.append(f'{path}/Connector/')
sys.path.append(f'{path}/Planning/')
sys.path.append(f'{path}/Message/')
sys.path.append(f'{path}/User/')
sys.path.append(f'{path}/Event')
import resources as res
import user_service as usr_serv
import event_service as event_serv
import message_service as msg_serv
import planning_service as plan_serv
from  user import User
from event import Event, Location
import keys

# TO DO LIST 
# AJOUTER UN talbe pour lister les chan autorisé pour le bot


bot = Bot(command_prefix = res.commandSign)

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"Logged in as {bot.user}!")
    print('We have logged in as {0.user}'.format(bot))
    print('\n\n!planning-Sea Of Thieves-4-20h30-here')   


@bot.command(name='test', help="test a default event")
async def DefaultPlanning(ctx):
    
    authorDb = await usr_serv.get_or_create_user(ctx.message.author)
    event = await event_serv.get_by_id(153)

    #bot_message = await ctx.message.channel.send(
    #    type = 1,
    #    embed=msg_serv.BuildInvitMessage(event, authorDb),
    #    components = [
    #        Button(disabled=0, label=res.button['ok'], style = 3, id=res.button['ok']),
    #        Button(disabled=0, label=res.button['cancel'], style = 4, id=res.button['cancel'])
    #    ]
    #)

    bot_message = await msg_serv.default_event_message_send(ctx.message.channel, bot, event, authorDb, Color.gold(), True, False)

    ppl = 1
    while ppl < event.slots:
        interaction = await bot.wait_for("button_click")

        if interaction.component.label == res.button['ok']:
            await interaction.respond(content=res.msg_dict['added'])
            ppl += 1
        else:
            await interaction.respond(content="correctly cancel")
            await bot_message.edit(
                type = 1,
                embed=msg_serv.BuildInvitMessage(event, authorDb, Color.red()),
                components=[]
            )
            return

    await ctx.message.channel.send("Done")


# Registering Receving Message event
@bot.event
async def on_message(message):
    # def tool
    if message.content.startswith(res.commandSign):
        await bot.process_commands(message)
    elif str(message.channel.type) == res.msg_type['dm'] and message.author != bot.user:
        await plan_serv.building_together(message, bot)
        

def CreatePlayerList(author):
    global players

    players = list()
    players.append(author)

def AddUserToEvent(user):
    if len(players) < slots:
        players.append(user.name)

def RemoveUserFromEvent(user):
    global author

    players.remove(user.name)
    if user.name == author and len(players) > 0:
        author = players[0]

async def UpdateCurrentEvent(payload):
    print("\n\n-----------------------  TO DO ---------------------------\n\n")
    return 
    global msg_dict, channel
    user = bot.get_user(payload.user_id)

    if payload.emoji.name == res.emojis_dict['cross'] and payload.user_id == author.id:
        await plan_serv.CancelCurrentEvent(message)
        return
    if payload.emoji.name == res.emojis_dict['thumbs_up'] and not user.name in players:
        AddUserToEvent(user)
    elif payload.emoji.name == res.emojis_dict['thumbs_down'] and user.name in players:
        RemoveUserFromEvent(user)
        if len(players) == 0:
            await plan_serv.CancelCurrentEvent(message)
            return

@bot.command()
async def default(ctx):
    await ctx.channel.send('>>> Commande inconnue. Utilisez !help pour de l\'aide')

@bot.command(name=res.clear, help=res.help['clear'])
async def clear(ctx):
    await msg_serv.FullClear(ctx.message)

@bot.command(name=res.cancel, help=res.help['cancel'])
async def clear(ctx):
    message = ctx.message
    await plan_serv.CancelCurrentEvent(message)
    await msg_serv.FullClear(message)

@bot.command(name=res.planning, help=res.help['planning'])
async def PlanningCommand(ctx):
    message = ctx.message
    if str(message.channel.type) == res.msg_type['dm']:
        await message.channel.send(res.error['not_here'])
        return
    authorDb = await usr_serv.get_or_create_user(message.author)
   
    event = await event_serv.new_event(message, authorDb)
    if message.content != res.commandSign + res.planning:
        event = await event_serv.no_step(message.content, authorDb, event)
        await message.channel.send(msg_serv.BuildInvitMessage(event, authorDb))
        return
    else:
        event.step = res.steps['game_name']
        await event_serv.update_event(event)
        await message.author.send(res.msg_dict['game_name'])

# Run bot (arg is the bot token)
bot.run(keys.botToken)
