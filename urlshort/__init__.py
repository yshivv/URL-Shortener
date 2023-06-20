from flask import Flask
from flask_assets import Bundle, Environment


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "hd823hjdk892jwjkq"

    from . import urlshort

    app.register_blueprint(urlshort.bp)
    return app
