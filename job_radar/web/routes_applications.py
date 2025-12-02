# job_radar/web/routes_applications.py
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from job_radar.core.models import Application
from job_radar.core.applications import add_application_from_job, add_event
from job_radar.core.db import db

bp = Blueprint("applications", __name__, url_prefix="/applications")

@bp.route("/")
def list_applications():
    apps = Application.query.order_by(
        Application.priority.desc(), Application.created_at.desc()
    ).all()
    return render_template("applications/list.html", apps=apps)

@bp.route("/add")
def add_application():
    job_id = request.args.get("job_id", type=int)
    if not job_id:
        return "job_id required", 400

    app = add_application_from_job(job_id)
    add_event(app, "CREATED", "Application created from job dashboard.")
    return redirect(url_for("applications.edit_application", app_id=app.id))

@bp.route("/<int:app_id>/edit", methods=["GET", "POST"])
def edit_application(app_id: int):
    app = Application.query.get_or_404(app_id)
    if request.method == "POST":
        old_status = app.status

        app.status = request.form.get("status", app.status)
        app.priority = int(request.form.get("priority", app.priority))
        app.notes = request.form.get("notes", app.notes)

        next_action_raw = request.form.get("next_action_date", "").strip()
        if next_action_raw:
            app.next_action_date = datetime.fromisoformat(next_action_raw)
        else:
            app.next_action_date = None

        if app.status == "applied" and not app.applied_at:
            app.applied_at = datetime.utcnow()

        db.session.commit()

        if app.status != old_status:
            add_event(app, f"STATUS_{app.status.upper()}", f"Status changed from {old_status} to {app.status}.")

        return redirect(url_for("applications.list_applications"))

    return render_template("applications/edit.html", app=app)
