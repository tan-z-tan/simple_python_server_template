import os
import flask


def make_app() -> flask.Flask:
    app = flask.Flask(os.getenv("APP_NAME"))

    @app.route("/ping")
    def ping():
        return "pong"

    return app


# Load configurations and initialize app with them
app = make_app()
