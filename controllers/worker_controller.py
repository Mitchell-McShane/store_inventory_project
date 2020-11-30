from flask import Flask, Blueprint, render_template
from models.worker import Worker
import repositories.worker_repository as worker_repository
import repositories.game_repository as game_repository

workers_blueprint = Blueprint("workers", __name__)

@workers_blueprint.route("/workers/staff")
def workers():
    worker = worker_repository.select_all()
    return render_template("/workers/staff.html", all_workers=worker)
