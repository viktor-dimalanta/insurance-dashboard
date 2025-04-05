# backend/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Client, Quote
from sqlalchemy.orm import Session
import models
import schemas
from schemas import QuoteCreate

async def create_client(db: AsyncSession, name: str, email: str) -> Client:
    # Create new client instance
    new_client = Client(name=name, email=email)
    db.add(new_client)
    await db.commit()
    await db.refresh(new_client)  # Refresh the object to get the generated ID
    return new_client

async def get_clients(db: AsyncSession):
    result = await db.execute(select(Client))
    return result.scalars().all()

async def get_client_quotes(db: AsyncSession, client_id: int):
    result = await db.execute(select(Quote).filter(Quote.client_id == client_id))
    return result.scalars().all()

async def create_quote(db: AsyncSession, quote: QuoteCreate):
    # Create a new quote object
    db_quote = Quote(amount=quote.amount, client_id=quote.client_id, quote_text=quote.quote_text)
    
    # Add it to the session and commit
    db.add(db_quote)
    await db.commit()
    await db.refresh(db_quote)  # To ensure the new ID is populated
    
    return db_quote

def get_quotes_for_client(db: Session, client_id: int):
    return db.query(models.Quote).filter(models.Quote.client_id == client_id).all()