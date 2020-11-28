from flask import Flask, render_template

from controllers.game_controller import games_blueprint
from controllers.worker_controller import workers_blueprint
from controllers.studio_controller import studios_blueprint

app = Flask(__name__)

app.register_blueprint(games_blueprint)
app.register_blueprint(workers_blueprint)
app.register_blueprint(studios_blueprint)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)