from db.run_sql import run_sql

from models.game import Game
import repositories.worker_repository as worker_repository
import repositories.studio_repository as studio_repository

# SAVE
def save(game):
    sql = "INSERT INTO games (name, worker_id, genre, price, buying_cost, stock, studio_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [game.name, game.worker.id, game.genre, game.price, game.buying_cost, game.stock, game.studio.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    game.id = id
    return game

# SELECT ALL 
def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)
    for row in results:
        studio = studio_repository.select(row['studio_id'])
        worker = worker_repository.select(row['worker_id'])

        game = Game(row['name'], worker, row['genre'], row['price'],row['buying_cost'], row['stock'], studio, row['id'])
        games.append(game)
    return games

# SELECT ID
def select(id):
    game = None
    sql = "SELECT * FROM games WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        worker = worker_repository.select(result['worker_id'])
        studio = studio_repository.select(result['studio_id'])
        game = Game(result['name'], worker, result['genre'], result['price'],result['buying_cost'], result['stock'], studio, result['id'])
    return game

# DELETE ALL
def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

# DELETE single id
def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# UPDATE 
def update(game):
    sql = "UPDATE games SET (name, worker_id, genre, price, buying_cost, stock, studio_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [game.name, game.worker.id, game.genre, game.price, game.buying_cost, game.stock, game.studio.id]
    run_sql(sql, values) 