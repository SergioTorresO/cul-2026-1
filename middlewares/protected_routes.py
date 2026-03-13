from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")

        if user_id is None:
            raise HTTPException(status_code=401)
        
        return payload

    except:
        raise HTTPException(status_code=401)

def require_role(role_id):

    def role_checker(user = Depends(get_current_user)):

        if user["rol"] != role_id:
            raise HTTPException(status_code=403, detail="Permiso denegado")

        return user

    return role_checker