import game_repository as repo
from game import Game

async def known_game(name):
    name=name.lower().capitalize()
    game_db = await repo.get_game_by_name(name)
    return game_db

async def get_game(id):
    return await repo.get_game(id)

async def add_image(game_id, image_url):
    return await repo.update_image_by_id(game_id, image_url)
