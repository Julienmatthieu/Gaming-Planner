import discord 

import user_repository as usr_rep
from user import User

async def get_or_create_user(author):
    userDb = usr_rep.get_user_discordId(author.id)
    if userDb == None:
        user = User(0, author.name, author.id, author.avatar_url, author.display_name, author.mention)
        return await usr_rep.create_user(user)
    else: 
        return userDb
