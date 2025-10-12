from fastapi import FastAPI, HTTPException
from .db import database
from . import crud, schemas
import os
import httpx

USER_SERVICE_URL = os.getenv('USER_SERVICE_URL', 'http://localhost:8001')

app = FastAPI(title='order-service')

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get('/health')
async def health():
    return {'status': 'ok'}

@app.post('/orders', response_model=schemas.Order)
async def create_order(order: schemas.OrderCreate):
    # Validate user exists by calling user-service
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{USER_SERVICE_URL}/users/{order.user_id}")
        if r.status_code == 404:
            raise HTTPException(status_code=400, detail='invalid user')
        r.raise_for_status()

    created = await crud.create_order(order.user_id, order.item)
    return created

@app.get('/orders/{order_id}', response_model=schemas.Order)
async def read_order(order_id: int):
    o = await crud.get_order(order_id)
    if not o:
        raise HTTPException(status_code=404, detail='order not found')
    return o

@app.get('/orders', response_model=list[schemas.Order])
async def list_all():
    return await crud.list_orders()
