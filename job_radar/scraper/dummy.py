# job_radar/scraper/dummy.py
from datetime import datetime, timedelta
from job_radar.scraper.base import BaseScraper, ScrapedJob

class DummyScraper(BaseScraper):
    """Fake scraper just to test the pipeline."""

    def fetch_jobs(self):
        now = datetime.utcnow()
        return [
            ScrapedJob(
                title="Software Engineer, University Graduate",
                company="Google",
                location="Bangalore, India",
                employment_type="Full-time",
                apply_url="https://careers.google.com/jobs/results/12345",
                posted_at=now - timedelta(days=1),
                source="Google",
            ),
            ScrapedJob(
                title="ML Engineer Intern",
                company="Amazon",
                location="Hyderabad, India",
                employment_type="Internship",
                apply_url="https://www.amazon.jobs/en/jobs/56789",
                posted_at=now - timedelta(days=2),
                source="Amazon",
            ),
        ]
