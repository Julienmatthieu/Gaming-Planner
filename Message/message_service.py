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


    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.red())

    embed.set_author(name=author.display_name, icon_url=author.avatarUrl)

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