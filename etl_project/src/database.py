from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

def execute_query(query):
    with engine.connect() as connection:
        connection.execute(query)
