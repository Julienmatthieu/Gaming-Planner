import re
import location_repository as repo
import user_service as usr_serv

async def get_location_by_event(event):
    return await repo.get_location_by_event(event)

async def create_new_location(location):
    return await repo.create_location(location)

# to do addin author search
async def get_event_by_message_location(message):
    return repo.get_location_by_guild_and_channel(message.guild.id, message.channel.id)

async def update_location_message_id(message):

    for elem in message.embeds:
        print(elem.footer.text)
        event_id = int(re.search(r'\d+', elem.footer.text).group())
        print(f" my id is {event_id} and my message id is {message.id}")
        await repo.update_location_from_message(event_id, message)