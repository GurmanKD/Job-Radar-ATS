# job_radar/web/routes_jobs.py
from flask import Blueprint, render_template
from job_radar.core.models import Job

bp = Blueprint("jobs", __name__, url_prefix="/jobs")

@bp.route("/")
def list_jobs():
    jobs = Job.query.order_by(Job.first_seen_at.desc()).limit(200).all()
    return render_template("jobs/list.html", jobs=jobs)
