from threading import Thread

from flask import Flask, jsonify

from extensions import db
from core.machine_manager import machine

app = Flask(__name__)
app.config.from_object("config.Config")

db.init_app(app)


def run_machine():
    with app.app_context():
        machine.run()


thread = Thread(target=run_machine)
thread.start()


@app.route('/machine', methods=['GET'])
def get_machine_status():
    return jsonify({"status": machine.status, "last_order_number": machine.get_last_order_number()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
