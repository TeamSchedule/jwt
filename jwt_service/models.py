from pydantic import BaseModel


class Credentials(BaseModel):
    login: str
    password: str


class RefreshToken(BaseModel):
    token: str
