# job_radar/web/app.py
from flask import Flask, render_template
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

    from job_radar.web.routes_jobs import bp as jobs_bp
    from job_radar.web.routes_applications import bp as applications_bp

    app.register_blueprint(jobs_bp)
    app.register_blueprint(applications_bp)

    @app.route("/")
    def index():
        from job_radar.core.models import Job, Application
        jobs_count = Job.query.count()
        apps_count = Application.query.count()
        return render_template("index.html", jobs_count=jobs_count, apps_count=apps_count)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app
