import connector 
from user import User
from resources import databaseSeparator

async def get_user_discordId(discord_id):
    query = f"""SELECT * FROM user WHERE discordId = \"{discord_id}\""""
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    test =  User(row[0], row[1], row[2], row[3], row[4], row[5]) 
    return User(row[0], row[1], row[2], row[3], row[4], row[5]) 

async def create_user(user):
    query = f"""INSERT INTO user (name, discordId, avatarUrl, displayName, mention) VALUES (\"{user.name}\", \"{user.discord_id}\", \"{user.avatarUrl}\", \"{user.displayName}\", \"{user.mention}\")  """
    userId = connector.alter_query(query)
    user.id = userId
    return user

async def update_user(user):
    query = f"UPDATE user SET name = \"{user.name}\", avatarUrl = \"{user.avatarUrl}\", displayName = \"{user.displayName}\", mention = \"{user.mention}\" \
                    WHERE discordId = {user.id}"    
    print(f"------------------------------------------------------------\n")
    print(query)
    print(f"------------------------------------------------------------\n")
    connector.alter_query(query)
    return user 
    