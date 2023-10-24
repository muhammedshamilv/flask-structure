from flask import Blueprint
from todo.controllers.main import create_todo

todo_bp = Blueprint("todo", __name__, url_prefix="/user")


todo_bp.add_url_rule("/<int:user_id>/todo", view_func=create_todo, methods=["POST"])
