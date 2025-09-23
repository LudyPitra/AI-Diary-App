"""Main FastAPI application for the AI Diary backend.

This module initializes the FastAPI application, creates database tables,
and defines the main API endpoints for the diary application.
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
# --
from . import models, crud, schemas, security
from .database import SessionLocal, engine, Base

# Create all database tables based on the models
# This will create the tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    user = security.get_current_user(token=token, db=db)
    
    if not user:
        raise credentials_exception
    
    return user

origins = [
    "http://localhost:5173", # A URL do front-end em desenvolvimento
    "http://127.0.0.1:5173", # Variante comum do host local
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Lista de origens que podem fazer requisições
    allow_credentials=True,
    allow_methods=["*"], # Permite todos os métodos (GET, POST, etc)
    allow_headers=["*"], # Permite todos os cabeçalhos
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/token")
def login_for_access_token(
    request_data: schemas.TokenRequest, db: Session = Depends(get_db)
    ):
    
    user = crud.authenticate_user(db, email=request_data.email, password=request_data.password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.User)
def read_users_me(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
    ):
    return current_user

@app.get("/")
def read_root():
    """
    Root endpoint to check if the API is running.
    
    Returns:
        dict: A welcome message confirming the API is operational
    """
    return {"message": "Hello, AI Diary backend is running!"}

@app.get("/entries", response_model=List[schemas.Entry])
def read_entries(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
    ):
    entries = crud.get_entries(db=db, user_id=current_user.id)
    return entries

@app.post("/entries/", response_model=schemas.Entry)
def create_entry(
    entry: schemas.EntryCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
    ):
    return crud.create_user_entry(db=db, entry=entry, user_id=current_user.id)