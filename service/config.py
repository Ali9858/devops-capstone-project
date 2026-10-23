"""
Global Configuration for Application
"""
import os


# Use SQLite for local development unless an environment database is configured.
DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///accounts.db")

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")
