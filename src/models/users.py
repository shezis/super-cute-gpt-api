from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import relationship
from db_startup import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String)
    subscriptions = relationship('Subscription', back_populates='user')
