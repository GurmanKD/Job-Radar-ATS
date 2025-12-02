# job_radar/web/app.py
from flask import Flask
from job_radar.core.config import Config
from job_radar.core.db import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        from job_radar.core import models  # noqa: F401
        db.create_all()

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
