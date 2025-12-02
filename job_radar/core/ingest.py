# job_radar/core/ingest.py
from typing import List, Optional
from job_radar.core.db import db
from job_radar.core.models import Job
from job_radar.scraper.registry import SCRAPERS
from job_radar.core.filters import is_relevant
from job_radar.scraper.base import ScrapedJob

def _upsert_job(scraped: ScrapedJob) -> Optional[Job]:
    if not is_relevant(scraped):
        return None

    job = Job.query.filter_by(apply_url=scraped.apply_url).first()
    if job:
        # already in DB, just ignore as "not new"
        return None

    job = Job(
        title=scraped.title,
        company=scraped.company,
        location=scraped.location,
        employment_type=scraped.employment_type,
        apply_url=scraped.apply_url,
        posted_at=scraped.posted_at,
        source=scraped.source,
    )
    db.session.add(job)
    return job

def ingest_jobs() -> List[Job]:
    new_jobs: List[Job] = []
    for scraper in SCRAPERS:
        scraped_jobs = scraper.fetch_jobs()
        for sj in scraped_jobs:
            job = _upsert_job(sj)
            if job is not None:
                new_jobs.append(job)
    db.session.commit()
    return new_jobs
