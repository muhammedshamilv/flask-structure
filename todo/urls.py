from flask import Blueprint
from todo.controllers.main import create_todo, delete_todo, edit_todo, get_all_todo

todo_bp = Blueprint("todo_bp", __name__, url_prefix="/user")


todo_bp.add_url_rule("/<int:user_id>/todo", view_func=create_todo, methods=["POST"])
todo_bp.add_url_rule("/list/todo", view_func=get_all_todo, methods=["GET"])
todo_bp.add_url_rule("/todo/<int:todo_id>", view_func=delete_todo, methods=["DELETE"])
todo_bp.add_url_rule("/todo/<int:todo_id>", view_func=edit_todo, methods=["PUT"])
