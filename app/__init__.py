
# app/__init__.py

import os
from dotenv import load_dotenv

load_dotenv()

SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
APP_ENV = os.environ.get("APP_ENV")