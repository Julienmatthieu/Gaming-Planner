from event import Event
from user import User
from resources import msg_type 
from discord import Color, Embed

from discord.ext.commands import Bot
from discord_components import Button

import resources as res

# Event setting
def BuildInvitMessage(event, author, color=Color.gold()):
    if event == None:
        return ''

    embed=Embed(title=f"Let's play some event.gameName", description=f"I\'m looking for **{event.slots}** people(s) to join on **event.gameName**. \n\
                                Game session will start at **{event.time}**. ", color=color)
    # Add an image
    embed.set_thumbnail(url="https://compass-ssl.xboxlive.com/assets/1f/35/1f355aca-753c-4213-8a42-563128129070.jpg?n=Parallax_Sections_Large_Desktop_01.jpg")
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
            embed=BuildInvitMessage(event, authorDb, color),
            components = buttons
        )
    return await send_to.send(
            type = 1,
            embed=BuildInvitMessage(event, authorDb, color),
            components = buttons
    )

async def FullClear(message):
    if str(message.channel.type) == msg_type['dm']:
        return
    async for message in message.channel.history(limit=None):
        await message.delete()