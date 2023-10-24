from logging import Logger
from flask import request, jsonify
from middleware.auth import authenticate_required
from todo.models import Todo
from app import db


@authenticate_required
def create_todo(user, user_id):
    try:
        todo_json = request.get_json()
        new_todo = Todo(
            title=todo_json["task"],
            description=todo_json["description"],
            user_id=user_id,
        )
        db.session.add(new_todo)
        db.session.commit()
        return jsonify({"message": "Todo created successfully"}), 201
    except Exception as e:
        print("Error occurred", str(e))
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}), 500
