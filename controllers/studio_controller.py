from flask import Flask, Blueprint, render_template
from models.studio import Studio
import repositories.studio_repository as studio_repository

studios_blueprint = Blueprint("studios", __name__)