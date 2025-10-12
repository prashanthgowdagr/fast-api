from databases import Database
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql+asyncpg://appuser:postgrespw@localhost:5432/appdb')

database = Database(DATABASE_URL)
