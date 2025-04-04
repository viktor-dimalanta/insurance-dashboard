import logging
from fastapi import HTTPException, Request, status
from jose import JWTError, jwt
from config import JWT_SECRET, ALGORITHM
from datetime import datetime, timedelta
from typing import Dict
from fastapi import APIRouter
from pydantic import BaseModel

# Function to get the current user (extracts the JWT token from the Authorization header)
async def get_current_user(request: Request) -> Dict:
    token = request.headers.get("Authorization")
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authorization token missing",
        )
    
    # Split the "Bearer <token>" and extract the token
    token = token.split("Bearer ")[-1]

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token format",
        )
    
    return await verify_token(token)

# Function to verify the token
logging.basicConfig(level=logging.DEBUG)
async def verify_token(token: str) -> Dict:
    try:
        logging.debug(f"Decoding token: {token}")
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        logging.debug(f"Decoded payload: {payload}")

        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )
        return {"user_id": user_id}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

class Token(BaseModel):
    access_token: str
    token_type: str

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"sub": data.get("username")})
    
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm=ALGORITHM)
    return encoded_jwt

router = APIRouter()

@router.post("/token", response_model=Token)
async def generate_token(data: dict):
    username = data.get("username")
    if not username:
        raise HTTPException(status_code=400, detail="Username is required")
    token = create_access_token(data={"sub": username})
    return {"access_token": token, "token_type": "bearer"}