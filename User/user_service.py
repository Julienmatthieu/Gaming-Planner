import discord 

import user_repository as repo
from user import User

async def get_or_create_user(author22222):
    print("\n\n --------------- 1 - 1 - 1 ---------------\n\n")
    
    userDb = await repo.get_user_discordId(author22222.id)
    print(f"\n\n --------------- 1 - 1 - 2--------------- {userDb.name}\n\n ")
    if userDb == None:
        user = User(0, author22222.name, author22222.id, author22222.avatar_url, author22222.display_name, author22222.mention)
        print("\n\n --------------- 1 - 1  - 3 - 1 ---------------\n\n")
        return await repo.create_user(user)
    else: 
        print("\n\n --------------- 1 - 1  - 3 - 2---------------\n\n")
        return userDb

