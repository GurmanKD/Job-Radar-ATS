# scripts/run_ingest.py
import os
import sys

# Add project root to sys.path so "job_radar" can be imported
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from job_radar.web.app import create_app  # noqa: E402
from job_radar.core.ingest import ingest_jobs  # noqa: E402

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        new_jobs = ingest_jobs()
        print(f"Ingested {len(new_jobs)} new jobs.")
        for j in new_jobs:
            print(f"- {j.company} | {j.title} | {j.location}")
