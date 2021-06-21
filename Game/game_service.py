import game_repository as repo
from game import Game

async def known_game(name):
    game_db = await repo.get_game_by_name(name)
    if game_db.image == "":
        return False
    else:
        return True

async def add_image(game_id, image_url):
    print("    ------------- adding image ------------------")
    return await repo.update_image_by_id(game_id, image_url)
