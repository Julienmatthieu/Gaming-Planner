import discord 

import user_repository as repo
from user import User

async def get_or_create_user(author):
    print("\n\n --------------- 1 - 1 - 1 ---------------\n\n")
    
    userDb = await repo.get_user_discordId(author.id)
    print("\n\n --------------- 1 - 1 - 2---------------\n\n")
    if userDb == None:
        user = User(0, author.name, author.id, author.avatar_url, author.display_name, author.mention)
        print("\n\n --------------- 1 - 1  - 3 - 1 ---------------\n\n")
        return await repo.create_user(user)
    else: 
        print("\n\n --------------- 1 - 1  - 3 - 1---------------\n\n")
        return userDb

