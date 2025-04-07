from pydantic import BaseModel
from typing import Optional

# ----- Client Schemas -----
class ClientBase(BaseModel):
    name: str
    email: str

class ClientCreate(ClientBase):
    pass

class ClientOut(ClientBase):
    id: int

    class Config:
        orm_mode = True

# ----- Quote Schemas -----
class QuoteBase(BaseModel):
    amount: int
    client_id: int  # assuming each quote belongs to a client
    quote_text: Optional[str] = None

# Model to create a new Quote (without id)
class QuoteCreate(QuoteBase):
    pass

# Model representing the Quote (including id)
class Quote(QuoteBase):
    id: int

class QuoteOut(QuoteCreate):
    id: int
    
    class Config:
        orm_mode = True