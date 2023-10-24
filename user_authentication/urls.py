from flask import Blueprint
from user_authentication.controllers.main import (
    HealthCheck,
    login_template,
    signup_template,
    create_user,
    login,
    home_template,
)

health_check_bp = Blueprint("health_check", __name__, url_prefix="/health")
login_bp = Blueprint("login", __name__, url_prefix="/")
health_check_bp.add_url_rule(
    "/", view_func=HealthCheck.as_view("health_check"), methods=["GET"]
)


login_bp.add_url_rule("/", view_func=login_template, methods=["GET"])
login_bp.add_url_rule("/signup", view_func=signup_template, methods=["GET"])
login_bp.add_url_rule("/create/account", view_func=create_user, methods=["POST"])
login_bp.add_url_rule("/user/login", view_func=login, methods=["POST"])
login_bp.add_url_rule("/home", view_func=home_template, methods=["GET"])
