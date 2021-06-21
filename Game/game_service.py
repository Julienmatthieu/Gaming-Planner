import game_repository as repo
from game import Game

async def known_game(name):
    game_db = await repo.get_game_by_name(name)
    if game_db.image == "":
        return False
    else:
        return True
