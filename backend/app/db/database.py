import os

from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv()

DATABASE_URL = os.environ.get("DATABASE_URL")
DATABASE_NAME = os.environ.get("DATABASE_NAME")

client = AsyncIOMotorClient(DATABASE_URL)

database = client[DATABASE_NAME]
user_collection = database.get_collection("users")
