"""Database models for the AI Diary application.

This module defines the SQLAlchemy ORM models for users and diary entries.
It establishes the database schema and relationships between entities.
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base


class User(Base):
    """User model representing registered users in the system.
    
    This model stores user authentication information and maintains
    a relationship with diary entries owned by the user.
    
    Attributes:
        id (int): Primary key, auto-incrementing user identifier
        email (str): Unique email address for user authentication
        hashed_password (str): Bcrypt hashed password for security
        is_active (bool): Flag to enable/disable user account
        entries (List[Entry]): Related diary entries owned by this user
    """
    __tablename__ = "users"
    
    # Primary key with automatic indexing for fast lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # Email must be unique and indexed for authentication queries
    email = Column(String, unique=True, index=True)
    
    # Store hashed password for security (never store plain text)
    hashed_password = Column(String)
    
    # Flag to enable/disable user accounts without deletion
    is_active = Column(Boolean, default=True)
    
    # One-to-many relationship: one user can have many entries
    entries = relationship("Entry", back_populates="owner")
    
class Entry(Base):
    """Diary entry model representing individual diary posts.
    
    This model stores diary entries with their content, metadata,
    and maintains a relationship with the user who created them.
    
    Attributes:
        id (int): Primary key, auto-incrementing entry identifier
        title (str): Title of the diary entry
        content (str): Main content/body of the diary entry
        created_at (datetime): Timestamp when entry was created
        owner_id (int): Foreign key referencing the user who owns this entry
        owner (User): Related user object who owns this entry
    """
    __tablename__ = "entries"
    
    # Primary key with automatic indexing for fast lookups
    id = Column(Integer, primary_key=True, index=True)
    
    # Entry title with indexing for search functionality
    title = Column(String, index=True)
    
    # Main content of the diary entry (can be long text)
    content = Column(String)
    
    # Automatic timestamp when entry is created (UTC timezone)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Foreign key linking to the user who owns this entry
    owner_id = Column(Integer, ForeignKey("users.id"))
    
    # Many-to-one relationship: many entries belong to one user
    owner = relationship("User", back_populates="entries")