from flask_restful import fields

extra_fields = {
    'number': fields.Integer,
    'cost': fields.Float,
    'description': fields.String,
    'duration': fields.Float,
}
