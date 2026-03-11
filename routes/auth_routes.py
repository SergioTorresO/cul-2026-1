from fastapi import APIRouter, HTTPException
from validations.login_validation import validate
from models.login_model import Login

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    user = {"email": email, "password": password}

    validation = validate(user)
    print("validation", validation)
    if "error" in validation:
        raise HTTPException(status_code=401, detail=validation["error"])

    return {
        "access_token": validation["access_token"],
        "token_type": "bearer"
    }