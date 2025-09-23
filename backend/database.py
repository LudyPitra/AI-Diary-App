"""Database configuration and setup for the AI Diary application.

This module configures the SQLAlchemy database connection, session management,
and provides the base class for all ORM models.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pathlib import Path

# SQLite database URL - stores the diary.db file in the backend directory
# Build an absolute path to avoid dependency on current working directory
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "diary.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is needed for SQLite to work with FastAPI
# This allows multiple threads to access the same SQLite connection
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a SessionLocal class for database sessions
# autocommit=False: Transactions must be explicitly committed
# autoflush=False: Changes are not automatically flushed to the database
# bind=engine: Bind sessions to our database engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for all ORM models
# All database models will inherit from this Base class
Base = declarative_base()
