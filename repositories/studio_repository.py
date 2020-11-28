from db.run_sql import run_sql

from models.studio import Studio
from models.worker import Worker
from models.game import Game

# CREATE
def save(studio):
    sql = "INSERT INTO studios (name) VALUES (%s) RETURNING id"
    values = [studio.name]
    results = run_sql(sql, values)
    studio.id = results[0]['id']
    return studio

# SELECT ALL
def select_all():
    studios = []
    sql = "SELECT * FROM studios"
    results = run_sql(sql)
    for row in results:
        studio = Studio(row['name'], row['id'])
        studios.append(studio)
    return studios

# SELECT ID
def select(id):
    studio = None
    sql = "SELECT * FROM studios WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        studio = Studio(result['name'], result['id'])
    return studio

# DELETE ALL
def delete_all():
    sql = "DELETE FROM studios"
    run_sql(sql)