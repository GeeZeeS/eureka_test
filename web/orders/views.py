from flask import request, jsonify, Blueprint
from flask_restful import marshal

from orders.constants import extra_fields
from orders.scripts import get_paginated_orders

orders_bp = Blueprint('orders', __name__)


@orders_bp.route('/api/orders', methods=['GET'])
def get_orders():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)

    orders = get_paginated_orders(page, per_page)

    result = {
        'orders': [marshal(order, extra_fields) for order in orders.items],
        'pagination': {
            'page': page,
            'per_page': per_page,
            'total_pages': orders.pages,
            'total_items': orders.total,
        }
    }

    return jsonify(result)
