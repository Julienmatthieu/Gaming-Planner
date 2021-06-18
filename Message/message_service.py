from event import Event
from user import User
from resources import msg_type 
import discord

# Event setting
def BuildInvitMessage(event, author):
    embed = discord.Embed()
    if event == None:
        return ''
    players = event.get_list_players()

    message = ""
    for slot in range(event.slots):
        if slot < len(players):
            message += f'\n\t  **➤ {players[slot]}**'
        else:
            message += f'\n\t  **➤** '
    embed.add_field(name=f"**{author.mention}** lance une session de  **{event.gameName}** ", value=f"**Heure:** **`{event.time}`\n**➤ Places:**{str(event.slots - len(players))}** \n", inline=True)
    embed.add_field(name=f"\n Participant: ", value=message, inline=False)

    return message

async def FullClear(message):
    if str(message.channel.type) == msg_type['dm']:
        return
    async for message in message.channel.history(limit=None):
        await message.delete()


       

        list = ""


        embed.add_field(name="Senna", value="**➤ Name:** `Senna`\n**➤ Level:** 5\n**➤ Points:** 24526", inline=True)
        await ctx.send(embed=embed)