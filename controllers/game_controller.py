from flask import Flask, Blueprint, render_template, redirect, request
from models.game import Game
import repositories.game_repository as game_repository
import repositories.studio_repository as studio_repository
import repositories.worker_repository as worker_repository

games_blueprint = Blueprint("games", __name__)

# INDEX
# GET '/games'
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", all_games=games)

# NEW
# GET '/games/new
@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    games = game_repository.select_all()
    return render_template("games/new.html", games=games)


# Show games info
@games_blueprint.route("/games/<id>")
def show_game(id):
    game = game_repository.select(id)
    return render_template("games/show.html", game=game)

# EDIT games info
@games_blueprint.route("/games/<id>/edit", methods=['GET'])
def edit_game(id):
    game = game_repository.select(id)
    worker = worker_repository.select_all()
    studio = studio_repository.select_all()
    return render_template("/games/edit.html", game=game, worker=worker, studio=studio)


# UPDATE games info
@games_blueprint.route("/games/<id>", methods=['POST'])
def update_game(id):
    print(request.form)
    name = request.form["name"]
    worker = worker_repository.select(request.form["worker_id"])
    genre = request.form["genre"]
    price = request.form["price"]
    buying_cost = request.form["buying_cost"]
    stock = request.form["stock"]
    studio = studio_repository.select(request.form["studio_id"])
    game = Game(name, worker, genre, price, buying_cost, stock, studio, id)
    print(game)
    game_repository.update(game)
    return redirect("/games")

# Deletes games record and sends management back to game stock page
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_games(id):
    game_repository.delete(id)
    return redirect("/games")
