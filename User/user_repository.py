import mysql.connector
from mysql.connector import Error
import sys
import pathlib
path = pathlib.Path().absolute()
sys.path.append(f'{path}/connector/')
import connector 
from user import User

async def get_user_discordId(discordId):
    query = f"""SELECT * FROM user WHERE discordId = \"{discordId}\""""
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    return User(row[0], row[1], row[2], row[3], row[4], row[5]) 

async def create_user(user):
    query = f"""INSERT INTO user (name, discordId, avatarUrl, displayName, mention) VALUES (\"{user.name}\", \"{user.discordId}\", \"{user.avatarUrl}\", \"{user.displayName}\", \"{user.mention}\")  """
    print(query)
    eventId = connector.alter_query(query)
    return eventId

