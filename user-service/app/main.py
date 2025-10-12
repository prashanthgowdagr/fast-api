from fastapi import FastAPI, HTTPException
from .db import database
from . import crud, schemas

app = FastAPI(title="user-service")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get('/health')
async def health():
    return {"status": "ok"}

@app.post('/users', response_model=schemas.User)
async def create_user(user: schemas.UserCreate):
    existing = await crud.get_user_by_email(user.email)
    if existing:
        raise HTTPException(status_code=400, detail='email exists')
    created = await crud.create_user(user.name, user.email)
    return {"id": created['id'], "name": created['name'], "email": created['email']}

@app.get('/users/{user_id}', response_model=schemas.User)
async def read_user(user_id: int):
    u = await crud.get_user(user_id)
    if not u:
        raise HTTPException(status_code=404, detail='user not found')
    return u

@app.get('/users', response_model=list[schemas.User])
async def list_all():
    return await crud.list_users()
