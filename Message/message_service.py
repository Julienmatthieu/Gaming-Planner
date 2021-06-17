from event import Event
from user import User

# Event setting
def BuildInvitMessage(event, author):
    if event == None:
        return ''
    players = event.get_list_players()

    message= f'@{event.role} '         
    message += f'\n>>> \n\t**{author.displayName}** lance une session de  **{event.gameName}**  <@!225743846934446081> '
    message += f'\n\t\theure:  **{event.time}** \t\t **{str(event.slots - len(players))}** place(s)\n'
    for slot in range(event.slots):
        if slot < len(players):
            message += f'\n\t  - {players[slot]}'
        else:
            message += f'\n\t  - '
    message += '\n\n   '
    return message

async def ClearHisto(channel):
    async for message in channel.history(limit=2):
            await message.delete()

async def FullClear(channel):
    async for message in channel.history(limit=None):
                await message.delete()