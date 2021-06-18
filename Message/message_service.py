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
    players = event.get_list_players()

    embed=Embed(title=f"Let's play some {event.gameName}", description=f"I\'m looking for **{event.slots}** people(s) to join on **{event.gameName}**. \n\
                                Game session will start at **{event.time}**. @{event.role} ", color=color)
    # Add an image
    #embed.set_thumbnail(url="https://compass-ssl.xboxlive.com/assets/1f/35/1f355aca-753c-4213-8a42-563128129070.jpg?n=Parallax_Sections_Large_Desktop_01.jpg")
    embed.set_author(name=author.displayName, icon_url=author.avatarUrl)
    message = ""
    for slot in range(event.slots):
        if slot < len(players):
            message += f'\n\t  - **{players[slot]}**'
        else:
            message += f'\n\t - '

    embed.add_field(name="Team:", value=message, inline=True)
    embed.set_footer(text=f"Thank you for using Game-planner bot. (event id:{event.id})")

    return embed

async def default_event_message_send(send_to, bot, event, authorDb, color=Color.gold(), button = True, is_edit=False):

    bot_message = await send_to.send(
        type = 1,
        embed=BuildInvitMessage(event, authorDb, color),
        components = [
            Button(disabled=0, label=res.button['ok'], style = 3, id=res.button['ok']),
            Button(disabled=0, label=res.button['cancel'], style = 4, id=res.button['cancel'])
        ]
    )

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

async def FullClear(message):
    if str(message.channel.type) == msg_type['dm']:
        return
    async for message in message.channel.history(limit=None):
        await message.delete()