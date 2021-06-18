from event import Event
from user import User
from resources import msg_type 
import discord

# Event setting
def BuildInvitMessage(event, author):
    #embed = discord.Embed()
    if event == None:
        return ''
    players = event.get_list_players()

    embed=discord.Embed(title=f"Let's play some {event.gameName}", description=f"I\'m looking for **{event.slots}** people(s) to join on **{event.gameName}**. \n\
                                Game session will start at **{event.time}**. @{event.role} ", color=discord.Color.gold())
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

#    embed.add_field(name=f"**{author.mention}** lance une session de  **{event.gameName}** ", value=f"**Heure:** **`{event.time}`\n**➤ Places:**{str(event.slots - len(players))}** \n", inline=True)
#    embed.add_field(name=f"\n Participant: ", value=message, inline=False)

    return embed

async def FullClear(message):
    if str(message.channel.type) == msg_type['dm']:
        return
    async for message in message.channel.history(limit=None):
        await message.delete()