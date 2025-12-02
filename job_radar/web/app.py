# job_radar/web/app.py
from flask import Flask
from job_radar.core.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
