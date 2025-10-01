"""CRUD (Create, Read, Update, Delete) operations for the AI Diary application.

This module contains database operations for managing users and diary entries.
All functions interact with the database through SQLAlchemy ORM sessions.
"""

from sqlalchemy.orm import Session
from . import models, schemas, security


def get_user_by_email(db: Session, email: str):
    """Retrieve a user by their email address.
    
    Args:
        db (Session): Database session for executing queries
        email (str): Email address to search for
        
    Returns:
        User | None: User object if found, None if not found
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user account with hashed password.
    
    Args:
        db (Session): Database session for executing queries
        user (schemas.UserCreate): User data containing email and password
        
    Returns:
        User: The newly created user object with generated ID
    """
    # Hash the password before storing it.
    hashed_password = security.get_password_hash(user.password)
    
    # Create a new user instance.
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    
    # Add, commit, and refresh the user in the database.
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user

def authenticate_user(db: Session, email: str, password: str):
    """Authenticate a user by their email and password."""
    
    user = get_user_by_email(db, email=email)
    if not user:
        return False
    
    if not security.verify_password(password, user.hashed_password):
        return False
    
    return user

def get_entries(db: Session, user_id: int):
    """Retrieve all diary entries for a specific user."""
    return db.query(models.Entry).filter(models.Entry.owner_id == user_id).all()
    
def create_user_entry(db: Session, entry: schemas.EntryCreate, user_id: int):
    """Create a new diary entry for a specific user."""
    db_entry = models.Entry(**entry.model_dump(), owner_id=user_id)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return db_entry