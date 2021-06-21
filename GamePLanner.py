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
sys.path.append(f'{path}/Game')
import resources as res
import user_service as usr_serv
import event_service as event_serv
import message_service as msg_serv
import planning_service as plan_serv
from  user import User
import keys

# TO DO LIST 
# AJOUTER UN talbe pour lister les chan autorisé pour le bot
bot = Bot(command_prefix = res.commandSign)

@bot.event
async def on_ready():
    DiscordComponents(bot)
    print(f"Logged in as {bot.user}!")
    print('We have logged in as {0.user}'.format(bot))
    print('\n!planning-Sea Of Thieves-4-20h30-here')   

# Registering Receving Message event
@bot.event
async def on_message(message):
    if message.content.startswith(res.commandSign):
        await bot.process_commands(message)
    elif str(message.channel.type) == res.msg_type['dm'] and message.author != bot.user:
        await plan_serv.building_together(message, bot)

@bot.command(name=res.next, help=res.help['next'])
async def next(ctx):
    message = ctx.message
    await plan_serv.pass_event_image(message)

@bot.command()
async def default(ctx):
    await ctx.channel.send('>>> Commande inconnue. Utilisez !help pour de l\'aide')

@bot.command(name=res.clear, help=res.help['clear'])
async def clear(ctx):
    await msg_serv.FullClear(ctx.message)

@bot.command(name=res.cancel, help=res.help['cancel'])
async def cancel(ctx):
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
    event.step = res.steps['game_name']
    await event_serv.update_event(event)
    await message.author.send(res.msg_dict['game_name'])
    await message.delete()

# Run bot (arg is the bot token)
bot.run(keys.botToken)
