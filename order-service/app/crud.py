from .models import orders
from .db import database

async def create_order(user_id: int, item: str):
    query = orders.insert().values(user_id=user_id, item=item)
    order_id = await database.execute(query)
    return {"id": order_id, "user_id": user_id, "item": item}

async def get_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    return await database.fetch_one(query)

async def list_orders():
    query = orders.select()
    return await database.fetch_all(query)
