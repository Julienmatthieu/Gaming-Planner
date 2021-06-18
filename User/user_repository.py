import connector 
from user import User

async def get_user_discordId(discordId):
    query = f"""SELECT * FROM user WHERE discordId = \"{discordId}\""""
    records = connector.select_query(query)
    if len(records) == 0:
        return None
    row = records[0]
    return User(row[0], row[1], row[2], row[3], row[4], row[5]) 
