# job_radar/core/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-change-me")

    # DB
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///job_radar.db")
    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

    # Email (for digests later)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", "587"))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")  # bot email
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    MAIL_FROM = os.getenv("MAIL_FROM", MAIL_USERNAME)
    MAIL_TO = os.getenv("MAIL_TO")  # your personal email for digests

    # Gmail sync
    GMAIL_USER_ID = "me"
    GMAIL_LABEL = os.getenv("GMAIL_LABEL", "job-applications")
