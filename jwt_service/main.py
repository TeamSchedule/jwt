import jwt
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .models import Credentials, RefreshToken
from .tokens import JWTAccess, JWTRefresh


app = FastAPI()


@app.post("/jwt/obtain")
async def obtain_token_pair(credentials: Credentials):
    credentials = credentials.dict()

    # TODO: check cred is valid
    is_valid = True

    if not is_valid:
        return JSONResponse(status_code=401, content={"error_message": "Incorrect login or password"})

    token_pair = {
        "access": JWTAccess.gen_token(credentials),
        "refresh": JWTRefresh.gen_token(credentials),
    }
    return token_pair


@app.post("/jwt/refresh")
async def refresh_token_pair(refresh_token: RefreshToken):
    token = refresh_token.token

    is_valid = JWTRefresh.validate(token)
    if not is_valid:
        return JSONResponse(status_code=401, content={"error_message": "Refresh token is not valid"})

    payload = jwt.decode(token, options={"verify_signature": False})

    token_pair = {
        "access": JWTAccess.gen_token(payload),
        "refresh": JWTRefresh.gen_token(payload),
    }
    return token_pair
