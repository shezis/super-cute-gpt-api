
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from db_startup import Base

class ServiceSubscription(Base):
    __tablename__ = 'service_subscription'
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey('services.id'))
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    subscription = relationship('Subscription', back_populates='service_subscription')
    service = relationship('Service', back_populates='service_subscription')
