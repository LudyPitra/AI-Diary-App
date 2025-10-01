"""
Password security utilities for the AI Diary application.

This module provides secure password hashing and verification functions
using bcrypt algorithm through the passlib library.
"""

from passlib.context import CryptContext
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from .setting import settings
from . import crud


# Initialize password context with bcrypt hashing scheme
# bcrypt is a secure, adaptive hashing function designed for passwords
# "deprecated=auto" automatically handles deprecated hash formats
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain text password against a hashed password.
    
    This function is used during user authentication to check if the provided password matches the stored hashed password.
    
    Args:
        plain_password (str): The plain text password to verify
        hashed_password (str): The stored bcrypt hash to verify against
        
    Returns:
        bool: True if password matches, False otherwise
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    Generate a secure bcrypt hash for a plain text password.
    
    This function is used when creating new users or updating passwords to securely store the password hash instead of plain text.
    
    Args:
        password (str): The plain text password to hash
        
    Returns:
        str: The bcrypt hash of the password
    """
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """
    Create a JWT access token with an expiration time.

    Args:
        data (dict): The data to encode in the token (e.g., user identifier).

    Returns:
        str: The encoded JWT access token.
    """

    to_encode = data.copy()
    # Set the token expiration time.
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # Encode the token with the secret key and algorithm.
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def get_current_user(db: Session, token: str):
    """
    Decode a JWT token to retrieve the current user.

    Args:
        db (Session): The database session.
        token (str): The JWT access token.

    Returns:
        User | None: The user object if the token is valid and the user exists, otherwise None.
    """
    try:
        # Decode the JWT to get the payload.
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        # Extract the email (subject) from the payload.
        email: str = payload.get("sub")
        if email is None:
            return None
    except JWTError:
        # Return None if the token is invalid or expired.
        return None
    
    # Retrieve the user from the database.
    user = crud.get_user_by_email(db=db, email=email)
    
    return user
    