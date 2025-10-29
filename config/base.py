from sqlalchemy.orm import DeclarativeBase 

from sqlalchemy import create_engine, event

class Base(DeclarativeBase):
    pass

from .settings import DATABASE_CONFIG

engine = create_engine(DATABASE_CONFIG["url"], echo=DATABASE_CONFIG["echo"])

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()