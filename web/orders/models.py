from flask_admin.contrib.sqla import ModelView
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
    number = db.column_property(id)
    cost = Column(Integer, nullable=True)
    description = Column(Text, nullable=True)
    duration = Column(Float, nullable=True)
    _status = db.Column('status', db.Integer, default=0, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    finished_at = Column(DateTime(timezone=True))

    @property
    def status(self):
        status_mapping = {
            0: 'IDLE',
            1: 'IN_PROGRESS',
            2: 'DONE'
        }
        return status_mapping.get(self._status)


class OrderAdminView(ModelView):
    column_list = ['number', 'cost', 'description', 'duration', 'status', 'created_at', 'finished_at']
    column_sortable_list = ['number', 'cost', 'description', 'duration', 'created_at', 'finished_at']
    column_default_sort = ('number', True)
    form_columns = ['cost', 'description', 'duration']
    form_edit_rules = ['cost', 'description', 'duration']

