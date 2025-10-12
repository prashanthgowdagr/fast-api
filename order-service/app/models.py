from sqlalchemy import (Column, Integer, String, Table, MetaData, ForeignKey)

metadata = MetaData()

orders = Table(
    'orders', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, nullable=False),
    Column('item', String(200), nullable=False),
)
