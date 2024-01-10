from flask import Flask
from flask_migrate import Migrate

from machine.views import CustomAdminIndexView, machine_bp
from orders.views import orders_bp
from orders.models import Order, OrderAdminView
from extensions import db, admin, cors

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)
migrate = Migrate(app, db)

admin.init_app(app, index_view=CustomAdminIndexView())
admin.add_view(OrderAdminView(Order, db.session))

cors.init_app(app)

app.register_blueprint(orders_bp)
app.register_blueprint(machine_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
