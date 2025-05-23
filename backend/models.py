# backend/models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    quotes = relationship("Quote", back_populates="client")

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    quote_text = Column(String, nullable=True) 
    amount = Column(Integer)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="quotes")
