from sqlalchemy import create_engine
import os


POSTGRES_URL = os.environ.get('DATABASE_URL')
POSTGRES_USER = "postgres"
POSTGRES_PW = "3044344"
POSTGRES_DB = "courses"

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)

engine = create_engine(DB_URL)
