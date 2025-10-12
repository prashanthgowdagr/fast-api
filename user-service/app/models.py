from sqlalchemy import (Column, Integer, String, Table, MetaData)

metadata = MetaData()

users = Table(
    'users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column('email', String(200), nullable=False, unique=True),
)
