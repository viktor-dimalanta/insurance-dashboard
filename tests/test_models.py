import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.models import Base, Client, Quote

# Use an in-memory SQLite database for testing
DATABASE_URL = "sqlite:///:memory:"

# Set up test engine and session
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Run before each test: create tables
@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)  # Create tables
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)  # Drop tables after each test

# Test creating a client
def test_create_client(db_session):
    client = Client(name="Test Client", email="test@example.com")
    db_session.add(client)
    db_session.commit()

    saved = db_session.query(Client).filter_by(email="test@example.com").first()
    assert saved is not None
    assert saved.name == "Test Client"

# Test adding quotes to a client
def test_client_quotes_relationship(db_session):
    client = Client(name="Quote Owner", email="quote@example.com")
    quote1 = Quote(quote_text="First quote", amount=100)
    quote2 = Quote(quote_text="Second quote", amount=200)
    client.quotes.extend([quote1, quote2])

    db_session.add(client)
    db_session.commit()

    saved_client = db_session.query(Client).filter_by(email="quote@example.com").first()
    assert len(saved_client.quotes) == 2
    assert saved_client.quotes[0].quote_text == "First quote"
    assert saved_client.quotes[1].amount == 200
