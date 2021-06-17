import mysql.connector
from mysql.connector import Error
import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(f'{path}/connector/')
import connector 

async def create_user(user):
    query = f"""INSERT INTO user (name, discordId, avatarUrl, displayName, mention) VALUES (\"{user.name}\", \"{user.discordId}\", \"{user.avatarUrl}\", \"{user.displayName}\", \"{user.mention}\")  """
    eventId = connector.alter_query(query)
    return eventId

