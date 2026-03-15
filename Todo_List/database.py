from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Database path
SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosApp.db'

# Creating engine for database instance
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

