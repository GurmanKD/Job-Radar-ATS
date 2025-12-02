# job_radar/scraper/registry.py
from job_radar.scraper.dummy import DummyScraper

SCRAPERS = [
    DummyScraper(),
    # later: GoogleScraper(), MicrosoftScraper(), etc.
]
