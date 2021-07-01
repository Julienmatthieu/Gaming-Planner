import discord 

import user_repository as repo
from user import User

async def get_or_create_user(author_discord):
    author = User(0, author_discord.display_name, author_discord.id, author_discord.avatar_url, author_discord.display_name, author_discord.mention)
    userDb = await repo.get_user_discordId(author.id)
    if userDb == None:
        return await repo.create_user(author)
    else: 
        if userDb.need_update(userDb.need_update(author)):
            await repo.update_user(userDb)
            userDb.copy(author)
        return userDb

async def get_by_discord_id(discird_id):
    return await repo.get_user_discordId(discird_id)