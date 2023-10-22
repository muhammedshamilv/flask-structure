from flask import views, jsonify

from app import db
from base_app.models import User


class HealthCheck(views.MethodView):
    def get(self):
        return jsonify({"msg": "health ok"}), 200
