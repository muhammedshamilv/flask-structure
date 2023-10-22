from flask import Blueprint
from base_app.controllers.main import HealthCheck

health_check_bp = Blueprint("health_check", __name__, url_prefix="/")

health_check_bp.add_url_rule(
    "/", view_func=HealthCheck.as_view("health_check"), methods=["GET"]
)
