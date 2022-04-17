from pydantic import BaseModel


class Credentials(BaseModel):
    id: int
    login: str


class RefreshToken(BaseModel):
    token: str
