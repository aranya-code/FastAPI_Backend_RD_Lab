from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


# Creating Database path

# Sqlite database
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosApp.db'
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread': False})

# PostgreSQL database
SQLALCHEMY_DATABASE_URL = os.getenv('postgresql_url')
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# MySQL database
# SQLALCHEMY_DATABASE_URL = os.getenv('mysql_url')
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creating engine for database instance
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

