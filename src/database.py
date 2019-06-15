from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection
from sqlalchemy.orm import scoped_session, sessionmaker
from config import DB_USER, DB_PASSWORD, DB_NAME

connection_string = f"postgresql://{DB_USER}:{DB_PASSWORD}@127.0.0.1/{DB_NAME}"
engine = create_engine(connection_string)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base(cls=DeferredReflection)
Base.query = db_session.query_property()
