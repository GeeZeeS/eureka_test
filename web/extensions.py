from flask_admin import Admin
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
cors = CORS()
admin = Admin(name='Admin Panel', template_mode='bootstrap3')