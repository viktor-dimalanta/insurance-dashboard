from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from pydantic import BaseModel
from config import DATABASE_URL
from models import Base
from crud import get_clients, create_client, get_client_quotes,create_quote
from auth import get_current_user, create_access_token
from typing import List
from models import Quote
from schemas import QuoteOut
from fastapi.middleware.cors import CORSMiddleware

import models
import schemas
app = FastAPI()

# Set up CORS middleware to allow requests from localhost:3001
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # The front-end URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Database setup
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session

# Pydantic models
class ClientCreate(BaseModel):
    name: str
    email: str

class QuoteCreate(BaseModel):
    quote_text: str
    amount: int
    client_id: int

# Routes
@app.get("/clients")
async def list_clients(db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    clients = await get_clients(db)
    return clients

@app.post("/clients")
async def create_new_client(client: ClientCreate, db: AsyncSession = Depends(get_db), user: dict = Depends(get_current_user)):
    new_client = await create_client(db, client.name, client.email)
    return new_client

@app.get("/clients/{client_id}/quotes", response_model=List[QuoteOut])
async def get_quotes_for_client(client_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Quote).where(Quote.client_id == client_id))
    quotes = result.scalars().all()
    return quotes

@app.post("/quotes", response_model=QuoteOut)
async def create_quote_endpoint(
    quote: QuoteCreate,
    db: AsyncSession = Depends(get_db)
):
    db_quote = await create_quote(db=db, quote=quote)
    return db_quote
    
# Generate an access token (mocking MSAL auth)
@app.post("/token")
async def generate_token(data: dict):
    token = create_access_token(data)
    return {"access_token": token, "token_type": "bearer"}
