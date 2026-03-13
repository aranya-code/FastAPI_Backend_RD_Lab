from database import Base
from sqlalchemy import Column, Integer, Boolean, String

# Model for Todos list
class Todos_Model(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    status = Column(Boolean, default = False)
