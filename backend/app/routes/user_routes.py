from datetime import timedelta
import os

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.auth import authenticate_user
from app.auth.auth_bearer import JWTBearer, get_current_user
from app.auth.jwt_handler import create_access_token
from app.db.database import user_collection
from app.models.user import User
from app.utils.hashing import get_password_hash


router = APIRouter()


@router.post("/auth/login", tags=["auth"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email, username, or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=int(
        os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)))
    access_token = create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/auth/register", tags=["auth"])
async def signup(user: User):
    user_exist_email = await user_collection.find_one({"email": user.email})
    user_exist_username = await user_collection.find_one({"username": user.username})
    if user_exist_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    if user_exist_username:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    hashed_password = get_password_hash(user.password)
    new_user = {
        "username": user.username,
        "email": user.email,
        "password": hashed_password
    }
    await user_collection.insert_one(new_user)
    return {"msg": "User created successfully"}


@router.get("/users/me", tags=["users"])
async def get_user_info(current_user: dict = Depends(get_current_user)):
    # Assuming current_user contains the user's unique identifier (e.g., email or user_id)
    user_info = await user_collection.find_one({"email": current_user["sub"]})
    if user_info:
        # Return whatever information is appropriate; avoid returning passwords or sensitive data
        return {"username": user_info.get("username"), "email": user_info.get("email")}
    raise HTTPException(status_code=404, detail="User not found")


@router.get("/protected", dependencies=[Depends(JWTBearer())], tags=["users"])
async def protected_route():
    return {"msg": "This is a protected route"}
