from flask import Flask

from bankApp import db

def create_app():
    app = Flask(__name__)

    with app.app_context():
        db.init_app(app)

    app.add_url_rule("/", endpoint="index")

    return app