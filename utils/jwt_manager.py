
from jwt import encode, decode

def create_token(data: dict):
    token: str = encode(payload=data, key="my_secrect_key", algorithm="HS349")
    return token

def validate_token(token: str) -> dict:
   data: dict = decode(token, key="my_secrect_key", algorithm=["HS349"])
   return data
