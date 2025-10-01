"""Pydantic schemas for data validation and serialization in the AI Diary API.

This module defines the data models used for request/response validation,
serialization, and documentation in the FastAPI application.
"""

from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class EntryBase(BaseModel):
    """Base schema for diary entries containing common fields.
    
    This serves as the foundation for other entry-related schemas,
    containing the core fields that are shared across different operations.
    
    Attributes:
        title (str): The title of the diary entry
        content (Optional[str]): The main content/body of the entry (optional)
    """
    title: str
    content: Optional[str] = None


class EntryCreate(EntryBase):
    """Schema for creating new diary entries.
    
    Inherits all fields from EntryBase. Used when clients send
    data to create a new diary entry via the API.
    """
    pass


class Entry(EntryBase):
    """Complete diary entry schema including database fields.
    
    This schema represents a full diary entry as stored in the database,
    including auto-generated fields like ID and timestamps.
    
    Attributes:
        id (int): Unique identifier for the entry
        created_at (datetime): Timestamp when the entry was created
        owner_id (int): ID of the user who owns this entry
    """
    id: int
    created_at: datetime
    owner_id: int

    class Config:
        """Pydantic configuration to allow ORM mode."""
        from_attributes = True


class UserBase(BaseModel):
    """Base schema for users containing common fields.
    
    This serves as the foundation for other user-related schemas,
    containing the core fields that are shared across different operations.
    
    Attributes:
        email (str): User's email address (used for authentication)
    """
    email: str


class UserCreate(UserBase):
    """Schema for creating new user accounts.
    
    Extends UserBase with password field for user registration.
    The password will be hashed before storage for security.
    
    Attributes:
        password (str): Plain text password (will be hashed)
    """
    password: str


class User(UserBase):
    """Complete user schema including database fields and relationships.
    
    This schema represents a full user as stored in the database,
    including auto-generated fields and related diary entries.
    
    Attributes:
        id (int): Unique identifier for the user
        is_active (bool): Whether the user account is active
        entries (List[Entry]): List of diary entries owned by this user
    """
    id: int
    is_active: bool
    entries: List[Entry] = []

    class Config:
        """Pydantic configuration to allow ORM mode."""
        from_attributes = True

class TokenRequest(BaseModel):
    """Schema for requesting a token with email and password."""
    email: str
    password: str