from flask import Flask, Blueprint, render_template, redirect, request
from models.game import Game
import repositories.game_repository as game_repository
import repositories.studio_repository as studio_repository

games_blueprint = Blueprint("games", __name__)

# INDEX
# GET '/games'
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games=games)

# Deletes games record and sends management back to game stock page
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_games(id):
    game_repository.delete(id)
    return redirect("/games")
