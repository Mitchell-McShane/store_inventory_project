from db.run_sql import run_sql

from models.worker import Worker
from models.studio import Studio
from models.game import Game

# CREATE
def save(worker):
    sql = "INSERT INTO workers (name, age, dob) VALUES (%s, %s, %s) RETURNING id"
    values = [worker.name, worker.age, worker.dob]
    results = run_sql(sql, values)
    worker.id = results[0]['id']
    return worker

# SELECT ALL
def select_all():
    workers = []
    sql = "SELECT * FROM workers"
    results = run_sql(sql)
    for row in results:
        worker = Worker(row['name'], row['age'], row['dob'], row['id'])
        workers.append(worker)
    return workers

# SELECT ID
def select(id):
    worker = None
    sql = "SELECT * FROM workers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        worker = Worker(result['name'], result['age'], result['dob'], result['id'])
    return worker

# DELETE ALL
def delete_all():
    sql = "DELETE FROM workers"
    run_sql(sql)

# UPDATE
def games_by_worker(worker):
    games = []

    sql = "SELECT * FROM games WHERE worker_id = %s"
    values = [worker.id]
    results = run_sql(sql, values)

    for row in results:
        game = Game(row['name'], worker, row['genre'], row['price'],row['buying_cost'], row['stock'], row['studio_id'], row['id'])
        games.append(game)
    return games