from sqlalchemy import (
    func,
    Column,
    DateTime, Integer, Text, Float
)

from extensions import db


class Order(db.Model):
    __tablename__ = 'orders'

    IDLE = 0
    IN_PROGRESS = 1
    DONE = 2

    id = Column(Integer, primary_key=True, index=True)
    cost = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    duration = Column(Float, nullable=True)
    status = db.Column(db.Integer, default=0, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True))
