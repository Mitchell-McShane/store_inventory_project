from flask import Flask, Blueprint, render_template
from models.worker import Worker
import repositories.worker_repository as worker_repository
import repositories.game_repository as game_repository

workers_blueprint = Blueprint("workers", __name__)

@workers_blueprint.route("/workers/<id>")
def games(id):
    game = game_repository.select(id)
    worker = worker_repository.select(id)
    workers_games = worker_repository.games_by_worker(worker)
    return render_template("/games/show.html", all_workers=worker, all_games=game, workers_games=workers_games)