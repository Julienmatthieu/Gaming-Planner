#from os import name
import sys
import pathlib
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button


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




@bot.command(name='list')
async def button(ctx):
    await ctx.send(
        "Hello, World!",
        components = [
            Button(label = "WOW button!")
        ]
    )

    interaction = await bot.wait_for("button_click", check = lambda i: i.component.label.startswith("WOW"))
    await interaction.respond(content = "Button clicked!")


# Registering Loggin event
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print('\n\n!planning-Sea Of Thieves-4-20h30-here')   

# Registering Receving Message event
@bot.event
async def on_message(message):
    # def tool
    if message.content.startswith(res.commandSign):
        await bot.process_commands(message)
    elif message.author == bot.user and str(message.channel.type) != res.msg_type['dm']:
        await MessageFromBot(message)
    elif str(message.channel.type) == res.msg_type['dm'] and message.author != bot.user:
        await plan_serv.building_together(message, bot)

@bot.event
async def on_raw_reaction_add(payload):
    global even_message_id

    if payload.channel_id != channel.id or payload.message_id != even_message_id or payload.user_id == bot.user.id:
        return
    await UpdateCurrentEvent(payload)

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

@bot.command(name=res.clear, help =res.help['clear'])
async def clear(ctx):
    await msg_serv.FullClear(ctx.message)

@bot.command(name=res.cancel)
async def clear(ctx):
    message = ctx.message
    await plan_serv.CancelCurrentEvent(message)
    await msg_serv.FullClear(message)

@bot.command(name=res.planning)
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

async def MessageFromBot(message):
    event = await event_serv.get_last_unset_event(message)
    if event == None:
        return
    if event.step == res.steps['done']:
        emojis = [res.emojis_dict['thumbs_up'], res.emojis_dict['thumbs_down'], res.emojis_dict['cross']]
        for emoji in emojis:
            await message.add_reaction(emoji)

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