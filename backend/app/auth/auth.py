from app.db.database import user_collection
from app.utils.hashing import verify_password


async def authenticate_user(identifier: str, password: str):
    user = await user_collection.find_one({"$or": [{"email": identifier}, {"username": identifier}]})
    if not user:
        return False
    if not verify_password(password, user['password']):
        return False
    return user
