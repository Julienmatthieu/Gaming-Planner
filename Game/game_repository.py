from game import Game 
import time
import connector 

async def create_game(game):
    query = f"""INSERT INTO game (name, image) VALUES (\"{game.name}\",\"{game.image}\")"""
    game.id = connector.alter_query(query)
    return game

async def get_game_by_name(name):
    records = connector.select_query(f"""SELECT * FROM game WHERE name = \"{name}\"""")
    if len(records) == 0:
        return await create_game(Game(0, name, ""))
    row = records[0]
    game = Game(row[0], row[1], row[2]) 
    return game 

async def get_game(id):
    records = connector.select_query(f"""SELECT * FROM game WHERE id = {id}""")
    if len(records) == 0:
        return None
    row = records[0]
    game = Game(row[0], row[1], row[2]) 
    return game 

async def update_image_by_id(id, image_url):
    timestamp = time.strftime('%Y-%m-%d %H-%M-%S')

    query = f"""UPDATE game SET image = \"{image_url}\", on_update = \"{timestamp}\"  WHERE id = {id}"""
    connector.alter_query(query)
    return True   
