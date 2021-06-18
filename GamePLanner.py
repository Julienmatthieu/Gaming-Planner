#from os import name
import sys
import pathlib
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

    await ctx.message.channel.send(
        type = 1,
        embed=msg_serv.BuildInvitMessage(event, authorDb),
        components = [
            Button(disabled=0, label=res.button['ok'], style = 3, id=res.button['ok']),
            Button(disabled=0, label=res.button['cancel'], style = 4, id=res.button['cancel'])
            
        ]
    )
    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label == res.button['ok'])
    print("\n\n")
    print(interaction.custom_id)
    print("\n\n")
    await interaction.respond(content=res.msg_dict['added'])
#    if interaction.component.label == "I\'m in":
#        await interaction.message.edit(
#            type = 1,
#            embed=msg_serv.BuildInvitMessage(event, authorDb),
#            components = [
#                Button(disabled=0, label = "I\'m in 2 ", style = 3),
#                Button(disabled=0, label = "Cancel 2 ", style = 4)
#            ]
#        )
#    print("\n\n-----------\n")
#    print(interaction.__dict__)
#    print("\n\n-----------\n")

#    await interaction.channel.send(f"TEST Cliccked by {interaction.author.name} on {interaction.component.label} name  ")

#    while test == True:

#            test = False
#        else:
#            await interaction.channel.send(f"Cliccked by {interaction.author.name}")

@bot.command(name='list', help="test a changer")
async def button(ctx):
    await ctx.send(
        "Hello, World!",
        components = [
            Button(disabled=0, label = "Prymary", style = 1),
            Button(disabled=0, label = "Secondary 💀", style = 2),
            Button(disabled=0, label = "I\'m in 💪", style = 3),
            Button(disabled=0, label = "Cancel ❌", style = 4)
#               Button(disabled=1, label = "Link", style = 5, url='http://google.com'),
#               Button(disabled=0, label = "Prymary", style = 1),
#               Button(disabled=0, label = "Secondary", style = 2),
#               Button(disabled=0, label = "Success", style = 3),
#               Button(disabled=0, label = "Danger", style = 4),
#               Button(disabled=0, label = "Link", style = 5, url='http://google.com')         
        ]
    )
    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))
    await interaction.respond(content = "Button clicked!")
    # Note multi click 
    #while True:
    #    interaction = await <discord.ext.commands.Bot or discord.Client>.wait_for("button_click")
    #    await interaction.respond(content = "Wow")

# Registering Receving Message event
@bot.event
async def on_message(message):
    if message.content ==  "TEST":
        await message.channel.send("hello")

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
    await UpdateMessage(payload.message_id, bot.get_channel(payload.channel_id), msg_serv.BuildInvitMessage(None))

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

async def UpdateMessage(message_id, channel, content):
    message = await channel.fetch_message(message_id)
    await message.edit(content=content)

    if len(players) == slots:
        await message.clear_reactions()
        await message.add_reaction(res.emojis_dict['check'])
        await message.add_reaction(res.emojis_dict['cross'])
    elif planningStep == 5:
        await message.add_reaction(res.emojis_dict['thumbs_up'])
        await message.add_reaction(res.emojis_dict['thumbs_down'])
        await message.add_reaction(res.emojis_dict['cross'])

# Run bot (arg is the bot token)
bot.run(keys.botToken)
