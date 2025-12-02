# job_radar/core/applications.py
from datetime import datetime
from job_radar.core.db import db
from job_radar.core.models import Job, Application, ApplicationEvent

def add_application_from_job(job_id: int, priority: int = 3, notes: str = "") -> Application:
    job = Job.query.get(job_id)
    if not job:
        raise ValueError("Job not found")

    now = datetime.utcnow()
    app = Application(
        job_id=job.id,
        company=job.company,
        role_title=job.title,
        apply_url=job.apply_url,
        status="planned",
        created_at=now,
        last_updated_at=now,
        next_action_date=now,
        priority=priority,
        notes=notes,
    )
    db.session.add(app)
    db.session.commit()
    return app

def add_event(application: Application, event_type: str, description: str = "") -> ApplicationEvent:
    ev = ApplicationEvent(
        application_id=application.id,
        event_type=event_type,
        description=description,
    )
    db.session.add(ev)
    db.session.commit()
    return ev
