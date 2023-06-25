from flask import Flask
from flask_assets import Bundle, Environment


def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = "hd823hjdk892jwjkq"

    from . import urlshort

    app.register_blueprint(urlshort.bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
