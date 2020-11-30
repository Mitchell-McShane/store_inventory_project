from flask import Flask, Blueprint, render_template
from models.studio import Studio
import repositories.studio_repository as studio_repository
import repositories.game_repository as game_repository
import repositories.worker_repository as worker_repository

studios_blueprint = Blueprint("studios", __name__)

@studios_blueprint.route("/studios/<id>")
def games(id):
    game = game_repository.select(id)
    studio = studio_repository.select(id)
    studios_games = studio_repository.games_by_studio(studio)
    return render_template("/games/edit.html", all_studios=studio, all_games=game, 
    studios_games=studios_games)