
from sqlalchemy import Column, Integer, String,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from db_startup import Base

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String, unique=True, index=True)
    status = Column(Boolean, default=True)
    subscriptions = relationship('Subscription', back_populates='service')
    service_subscription = relationship('ServiceSubscription', back_populates='service')
