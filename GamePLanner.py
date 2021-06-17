from os import name
import discord 
import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(f'{path}/Ressources/')
sys.path.append(f'{path}/connector/event')
import ressources as res
import commands as com
import event_repository as event_rep
import keys
from event import Event, Location
 
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


# TO DO LIST 
# AJOUTER UN talbe pour lister les chan autorisé pour le bot


# TO DELETE AFTER UPDATE -----------------------------------------------
def BuildInvitMessageOld():
    global role, slots, gameName, date, author

    message= f'@{role} '         
    message += f'\n>>> \n\t**{author.name}** lance une session de  **{str(gameName)}**'
    message += f'\n\t\theure:  **{str(date)}** \t\t **{str(slots - len(players))}** place(s)\n'
    for slot in range(slots):
        if slot < len(players):
            message += f'\n\t- {players[slot]}'
        else:
            message += f'\n\t- '
    message += '\n\n   '
    return message

#global
channel= ''
even_message_id=None
planningStep=0
slots=-1
gameName=''
date=''
role=''
players= list()
author=None
# TO DELETE AFTER UPDATE -----------------------------------------------


# Registering Loggin event
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('\n\n!planning-Sea Of Thieves-4-20h30-here')   

# Registering Receving Message event
@client.event
async def on_message(message):
    global planningStep, slots, gameName, hours, min, even_message_id, channel

    if channel != '' and channel != message.channel or channel == '' and not message.content.startswith(com.commandSign):
        return

    # def tool
    if message.content.startswith(com.commandSign):
        await Commades(message)
    elif message.author == client.user and channel != '':
        await MessageFromBot(message)
    elif planningStep > 0 and channel != '':
        await Steps(message)
        return

@client.event
async def on_raw_reaction_add(payload):
    global even_message_id

    if payload.channel_id != channel.id or payload.message_id != even_message_id or payload.user_id == client.user.id:
        return
    await UpdateCurrentEvent(payload)

def CreatePlayerList(author):
    global players

    players = list()
    players.append(author)

#Steps
async def Steps(message):
    global planningStep, slots, gameName, date, role, author
    await message.delete()

    if planningStep == 1:
        gameName = message.content
        author = message.author
        planningStep = 2
        await UpdateMessage(even_message_id, message.channel, res.msg_dict['players'])
    elif planningStep == 2:
        slots = int(message.content)
        CreatePlayerList(message.author.name)
        planningStep = 3
        await UpdateMessage(even_message_id, message.channel, res.msg_dict['time'])
    elif planningStep == 3:
        date=message.content
        planningStep = 4
        await UpdateMessage(even_message_id, message.channel, res.msg_dict['role'])
    elif planningStep == 4:
        role = message.content
        planningStep = 5 
        await UpdateMessage(even_message_id, message.channel, BuildInvitMessageOld())

# Event setting
def BuildInvitMessage(event):
    players = event.get_list_players()

    message= f'@{event.role} '         
    message += f'\n>>> \n\t**{event.author}** lance une session de  **{event.gameName}**'
    message += f'\n\t\theure:  **{event.time}** \t\t **{str(event.slots - len(players))}** place(s)\n'
    for slot in range(event.slots):
        if slot < len(players):
            message += f'\n\t  - {players[slot]}'
        else:
            message += f'\n\t  - '
    message += '\n\n   '
    return message

def AddUserToEvent(user):
    if len(players) < slots:
        players.append(user.name)

def RemoveUserFromEvent(user):
    global author

    players.remove(user.name)
    if user.name == author and len(players) > 0:
        author = players[0]

async def UpdateCurrentEvent(payload):
    global msg_dict, channel
    user = client.get_user(payload.user_id)

    if payload.emoji.name == res.emojis_dict['cross'] and payload.user_id == author.id:
        await CancelCurrentEvent()
        return
    if payload.emoji.name == res.emojis_dict['thumbs_up'] and not user.name in players:
        AddUserToEvent(user)
    elif payload.emoji.name == res.emojis_dict['thumbs_down'] and user.name in players:
        RemoveUserFromEvent(user)
        if len(players) == 0:
            await CancelCurrentEvent()
            return
    await UpdateMessage(payload.message_id, client.get_channel(payload.channel_id), BuildInvitMessageOld())

#Comandes 
async def Commades(message):
    global planningStep, channel

    if message.content == com.commandSign + com.help:
        await message.channel.send(f'>>> Commades disponible:\
                                            \n\t{com.commandSign}{com.set_channel}: défini le chan d\'acttion du bot. A configurer a chaque redémarage\
                                            \n\t{com.commandSign}{com.unset_channel}: annule la configuration du chan\
                                            \n\t{com.commandSign}{com.planning} pour créer une session de jeu étape par étape\
                                            \n\t{com.commandSign}{com.planning}-GameName-NombreDeJoueurs-Date-Role pour créer une session en une seule commande\
                                            \n\t{com.commandSign}{com.clear}: supprime tous les messages du bot\
                                            \n\t{com.commandSign}{com.cancel}: annule la session en cours de création\
                                            \n\t{com.commandSign}{com.reset}: réinitialise les variable de l\évènement en cours. A utiliser si le bot est bloqué')
    elif message.content.startswith(com.commandSign + com.set_channel):
        channel = message.channel
        await channel.send(f">>> Je posterais à présent dans ce chan")
    elif channel == '':
        await message.channel.send(f'>>> Vous devez d\'abord m\'assigner a un chan. {com.commandSign}{com.set_channel}')
    elif message.content.startswith(com.commandSign + com.planning):
        await PlanningCommand(message)
    elif message.content == com.commandSign + com.clear:
        await FullClear(message.channel)
    elif message.content == com.commandSign + com.cancel:
        await CancelCurrentEvent()  
    elif message.content == com.commandSign + com.reset:
        if planningStep > 0:
            await CancelCurrentEvent()
    else:
        await message.channel.send('>>> Commande inconnue. Utilisez !help pour de l\'aide')
    await message.delete()

async def PlanningCommand(message):
    if message.content != com.commandSign + com.planning:
        await DirectPLanning(message)
        return
    else:
        await SimplePLanning(message)
        await message.channel.send(res.msg_dict['game_name'])

async def MessageFromBot(message):
    location = await event_rep.get_last_location(message.guild.id, message.channel.id)
    if (location == None):
        return
    location.messageId = message.id
    print(f" \n\n ASSIGNING THIS MESSAGE {message.id} to location {location.id}")
    await event_rep.update_location_message(location)
    event = event_rep.get_event(location.eventId)
    event.print()
    return
    if message.content.startswith('@'):
        if even_message_id == None:
            even_message_id = message.id
        emojis = [res.emojis_dict['thumbs_up'], res.emojis_dict['thumbs_down'], res.emojis_dict['cross']]
        for emoji in emojis:
            await message.add_reaction(emoji)
    elif planningStep != 0 and even_message_id == None: 
        even_message_id = message.id

async def SimplePLanning(message):
    new_event = Event(0, None, 0, None, message.author.name, message.author.name, None, step=res.build_steps['init'])
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    await event_rep.create_event(new_event, new_location)

    new_event.print()

async def DirectPLanning(message):
    data=message.content.split('-')
    author = message.author.name
    new_event = Event(id=0, gameName=data[1], slots=int(data[2]), time=data[3], author=author, player=author, role=data[4], step=res.build_steps['done'])
    new_location = Location(id = 0, guildId=message.guild.id, channelId=message.channel.id, messageId=0, eventId=0)
    await event_rep.create_event(new_event, new_location)
    # testing 
    await message.channel.send(BuildInvitMessage(new_event))
    await message.delete()

# Managing messages
async def CancelCurrentEvent():
    global even_message_id, channel

    if even_message_id == None:
        return 
    message = await channel.fetch_message(even_message_id)
    await message.edit(content=res.msg_dict[com.cancel])
    await message.clear_reactions()
    await message.add_reaction(res.emojis_dict['skull'])

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

async def ClearHisto(channel):
    async for message in channel.history(limit=3):
        if not message.content.startswith(f'{str(planningStep)}: '):
            await message.delete()

async def FullClear(channel):
    async for message in channel.history(limit=None):
            if message.author == client.user:
                await message.delete()

# Run bot (arg is the bot token)
client.run(keys.botToken)
