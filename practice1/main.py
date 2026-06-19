from fastapi import FastAPI
from pydantic import BaseModel

from .database import supabase
from .auth import create_access_token

app = FastAPI()


class User(BaseModel):
    email: str
    password: str


@app.get("/")
def home():
    return {"message": "FastAPI + JWT + Supabase"}


@app.post("/signup")
def signup(user: User):
    try:
        response = supabase.auth.sign_up(
            {
                "email": user.email,
                "password": user.password
            }
        )

        return {
            "message": "Signup successful",
            "user": str(response.user)
        }

    except Exception as e:
        return {"error": str(e)}


@app.post("/login")
def login(user: User):
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": user.email,
                "password": user.password
            }
        )

        if response.user is None:
            return {"error": "Invalid email or password"}

        token = create_access_token(
            {"sub": user.email}
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }

    except Exception as e:
        return {"error": str(e)}
