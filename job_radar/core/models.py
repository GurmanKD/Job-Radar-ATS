# job_radar/core/models.py
from datetime import datetime
from job_radar.core.db import db

class Job(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=True)
    employment_type = db.Column(db.String(100), nullable=True)
    apply_url = db.Column(db.String(1000), unique=True, nullable=False)
    posted_at = db.Column(db.DateTime, nullable=True)
    source = db.Column(db.String(255), nullable=False)

    first_seen_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_seen_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

class Application(db.Model):
    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey("jobs.id"), nullable=True)

    company = db.Column(db.String(255), nullable=False)
    role_title = db.Column(db.String(255), nullable=False)
    apply_url = db.Column(db.String(1000), nullable=False)

    status = db.Column(db.String(50), default="planned", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    applied_at = db.Column(db.DateTime, nullable=True)
    next_action_date = db.Column(db.DateTime, nullable=True)
    priority = db.Column(db.Integer, default=3, nullable=False)
    notes = db.Column(db.Text, default="", nullable=False)

    job = db.relationship("Job", backref="applications", lazy=True)

class ApplicationEvent(db.Model):
    __tablename__ = "application_events"

    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey("applications.id"), nullable=False)
    event_type = db.Column(db.String(100), nullable=False)
    event_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    description = db.Column(db.Text, default="", nullable=False)

    application = db.relationship("Application", backref="events", lazy=True)
