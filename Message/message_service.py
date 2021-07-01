from discord import Color, Embed
from discord.ext.commands import Bot
from discord_components import Button

from event import Event
from user import User
from game import Game
from resources import msg_type 
import game_service as game_serv
import resources as res

async def BuildInvitMessage(event, author, color=Color.gold()):
    if event == None:
        return ''

    game = await game_serv.get_game(event.game_id)
    embed=Embed(title=f"Let's play some {game.name}", description=f"I\'m looking for **{event.slots}** people(s) to join me on **{game.name}**. \n\
                                Game session will start at **{event.time}**. ", color=color)
    embed.set_thumbnail(url=game.image)
    embed.set_author(name=author.displayName, icon_url=author.avatarUrl)
    message = ""
    for slot in range(event.slots):
        if slot < len(event.players):
            message += f'\n\t  - **{event.players[slot]}**'
        else:
            message += f'\n\t - '

    embed.add_field(name="Team:", value=message, inline=True)
    embed.set_footer(text=f"Thank you for using Game-planner bot. (event id:{event.id})")

    return embed

async def send_or_edit_event_message(send_to, event, authorDb, color=Color.gold(), buttons=[] , is_edit=False):

    if is_edit:
        return await send_to.edit(
            type = 1,
            embed = await BuildInvitMessage(event, authorDb, color),
            components = buttons
        )
    return await send_to.send(
            type = 1,
            embed = await BuildInvitMessage(event, authorDb, color),
            components = buttons
    )

async def FullClear(message):
    if str(message.channel.type) == msg_type['dm']:
        return
    async for message in message.channel.history(limit=None):
        await message.delete()