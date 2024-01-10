import datetime
import random
import time

from core.models import Order
from extensions import db


class Machine:
    def __init__(self):
        self.order = None
        self.status = "OFF"
        self.last_order_number = 0

    @staticmethod
    def get_queue_order():
        order = Order.query.filter(
            Order.status != Order.DONE
        ).order_by(
            Order.id.asc() # noqa
        ).first()
        return order

    @staticmethod
    def generate_random():
        order = Order(
            cost=random.randint(10, 100),
            duration=random.randint(5, 20)
        )
        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def get_last_order_number():
        order = Order.query.filter(
            Order.status == Order.DONE
        ).order_by(
            Order.id.desc() # noqa
        ).first()
        if not order:
            return 0
        return order.id

    def run(self):
        while True:
            if not self.order or self.order.status == Order.DONE:
                self.order = self.get_queue_order()

            if not self.order:
                self.status = random.choice(["OFF", "STANDBY", "BUSY"])
                if self.status in ["OFF", "STANDBY"]:
                    time.sleep(3)
                    continue
                self.order = self.generate_random()

            self.update_status(Order.IN_PROGRESS)
            time.sleep(self.order.duration)
            self.update_status(Order.DONE)
            self.order.finished_at = datetime.datetime.now()
            db.session.commit()

    def update_status(self, status):
        self.order.status = status
        db.session.commit()


machine = Machine()
