from orders.models import Order


def get_paginated_orders(page, per_page):
    orders = Order.query.order_by(
        Order.id.desc() # noqa
    ).paginate(page=page, per_page=per_page, max_per_page=100, error_out=False)
    return orders
