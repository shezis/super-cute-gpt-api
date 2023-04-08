
from sqlalchemy import Column, Integer, ForeignKey,DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from db_startup import Base

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    service_id = Column(Integer, ForeignKey('services.id'))
    expiry_date = Column(DateTime)
    user = relationship('User', back_populates='subscriptions')
    service = relationship('Service', back_populates='subscriptions')
    service_subscription = relationship('ServiceSubscription', back_populates='subscription')
