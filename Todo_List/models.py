from database import Base
from sqlalchemy import Column, Integer, Boolean, String, ForeignKey

# Model for User
class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key= True, index= True)
    email = Column(String)
    username = Column(String, unique= True)
    name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default= True)
    role = Column(String)

# Model for Todos list
class Todos_Model(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    status = Column(Boolean, default = False)
    owner_id = Column(Integer, ForeignKey('users.id'))
