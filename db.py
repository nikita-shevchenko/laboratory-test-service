from sqlalchemy import create_engine
import os


DB_URL = os.environ.get('DATABASE_URL')

engine = create_engine(DB_URL)
