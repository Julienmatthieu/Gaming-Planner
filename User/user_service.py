import discord 

import user_repository as repo
from user import User

async def get_or_create_user(author_discord):
    author = User(0, author_discord.display_name, author_discord.id, author_discord.avatar_url, author_discord.display_name, author_discord.mention)
    userDb = await repo.get_user_discordId(author.discord_id)
    print("------------------------ 1 ")
    if userDb == None:
        print("------------------------ 2.1 ")
        return await repo.create_user(author)
    elif userDb.need_update(author):
        print("------------------------ 2.2.1 ---- Copy")
        userDb.print()
        userDb.copy(author)
        userDb.print()
        print("------------------------ 2.2.2 ")
        await repo.update_user(userDb)
        print("------------------------ 2.2.3 ")
    return userDb

async def get_by_discord_id(discird_id):
    return await repo.get_user_discordId(discird_id)