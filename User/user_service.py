import discord 

import user_repository as repo
from user import User

async def get_or_create_user(author):
    userDb = await repo.get_user_discordId(author.id)
    if userDb == None:
        user = User(0, author.display_name, author.id, author.avatar_url, author.display_name, author.mention)
        return await repo.create_user(user)
    else: 
        return userDb

async def get_by_discord_id(discird_id):
    return await repo.get_user_discordId(discird_id)