import location_repository as repo

async def get_location_by_event(event):
    return await repo.get_location_by_event(event)

async def create_new_location(location):
    return await repo.create_location(location)

async def update_location_message(location):
    return await repo.update_location_message(location)

# to do addin author search
async def get_event_by_message_location(message):
    return repo.get_location_by_guild_and_channel(message.guild.id, message.channel.id)
