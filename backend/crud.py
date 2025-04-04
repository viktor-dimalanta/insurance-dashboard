# backend/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Client, Quote

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
