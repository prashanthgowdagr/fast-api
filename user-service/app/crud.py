from .models import users
from .db import database

async def create_user(name: str, email: str):
    query = users.insert().values(name=name, email=email)
    user_id = await database.execute(query)
    return {"id": user_id, "name": name, "email": email}

async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

async def get_user_by_email(email: str):
    query = users.select().where(users.c.email == email)
    return await database.fetch_one(query)

async def list_users():
    query = users.select()
    return await database.fetch_all(query)
