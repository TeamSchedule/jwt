from abc import ABC
from datetime import datetime, timedelta, timezone

import jwt
from jwt.exceptions import InvalidTokenError

from .settings import JWT_SECRET_KEY


class BaseJWT(ABC):
    _ALGORITHM = "HS256"
    duration: timedelta = None
    token_type: str = None

    @classmethod
    def validate(cls, token: str) -> bool:
        try:
            jwt.decode(token, JWT_SECRET_KEY, algorithms=[cls._ALGORITHM])
            return True
        except InvalidTokenError:
            return False

    @classmethod
    def _get_exp_time(cls) -> int:
        if cls.duration is None:
            raise ValueError("Property `duration` must be specified!")
        return int((datetime.now(timezone.utc) + cls.duration).timestamp())

    @classmethod
    def _populate_payload(cls, credentials: dict) -> dict:
        credentials["exp"] = cls._get_exp_time()
        credentials["token_type"] = cls.token_type
        return credentials

    @classmethod
    def gen_token(cls, credentials: dict) -> str:
        if cls.duration is None or cls.token_type is None:
            raise ValueError("Property `duration` and `token_type` must be specified!")

        payload = cls._populate_payload(credentials)
        return jwt.encode(payload, JWT_SECRET_KEY, algorithm=cls._ALGORITHM)


class JWTAccess(BaseJWT):
    duration = timedelta(minutes=5)
    token_type = 'access'


class JWTRefresh(BaseJWT):
    duration = timedelta(days=30)
    token_type = 'refresh'
