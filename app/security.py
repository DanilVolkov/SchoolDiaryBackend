import jwt
from datetime import datetime, timedelta, timezone

from app.schemas.auth import TokenData
from app.config import settings

def create_access_token(data: TokenData, expires_delta: timedelta) -> str:
    to_encode = data.model_dump()
    expires = datetime.now(timezone.utc) + expires_delta
    to_encode.update({'exp': expires})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.HASH_ALGORITHM)
    return encoded_jwt
