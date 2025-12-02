# job_radar/scraper/base.py
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Any, Optional

class ScrapedJob:
    def __init__(
        self,
        title: str,
        company: str,
        location: str,
        employment_type: str,
        apply_url: str,
        posted_at: Optional[datetime],
        source: str,
        raw: Optional[Dict[str, Any]] = None,
    ):
        self.title = title
        self.company = company
        self.location = location
        self.employment_type = employment_type
        self.apply_url = apply_url
        self.posted_at = posted_at
        self.source = source
        self.raw = raw or {}

class BaseScraper(ABC):
    @abstractmethod
    def fetch_jobs(self) -> List[ScrapedJob]:
        """Return a list of ScrapedJob objects."""
        raise NotImplementedError
