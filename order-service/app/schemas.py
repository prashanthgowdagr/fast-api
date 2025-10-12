from pydantic import BaseModel

class OrderCreate(BaseModel):
    user_id: int
    item: str

class Order(BaseModel):
    id: int
    user_id: int
    item: str

    class Config:
        orm_mode = True
