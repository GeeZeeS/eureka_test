import requests
from flask import Blueprint
from flask_admin import AdminIndexView, expose

from config import Config
from orders.models import Order


machine_bp = Blueprint('machine', __name__)


class CustomAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        machine_data = requests.get(f"{Config.MACHINE_URI}/machine")
        last_5_orders = Order.query.order_by(
            Order.id.desc() # noqa
        ).limit(5).all()
        return self.render('index.html', machine_data=machine_data.json(), orders=last_5_orders)


@machine_bp.route('/api/machine', methods=['GET'])
def get_machine_info():
    machine_data = requests.get(f"{Config.MACHINE_URI}/machine")
    return machine_data.json()
