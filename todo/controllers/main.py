import datetime
from logging import Logger
from flask import request, jsonify
from middleware.auth import authenticate_required
from todo.models import Todo
from app import db
from todo.serializer import serialize_todo


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


@authenticate_required
def get_all_todo(
    user,
):
    try:
        tasks = Todo.query.filter_by(user_id=user).all()

        serialized_todo = [serialize_todo(todo) for todo in tasks]

        return jsonify({"todo": serialized_todo}), 200
    except Exception as e:
        print("Error occurred", str(e))
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}), 500


@authenticate_required
def delete_todo(user, todo_id):
    try:
        print("todo_id", todo_id)
        todo = Todo.query.filter_by(id=todo_id, user_id=user).first()

        if not todo:
            return jsonify({"message": "Todo not found"}, 404)

        db.session.delete(todo)
        db.session.commit()

        return jsonify({"message": "Todo deleted successfully"}), 200
    except Exception as e:
        print("Error occurred", str(e))
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}, 500)


@authenticate_required
def edit_todo(user, todo_id):
    try:
        todo = Todo.query.filter_by(id=todo_id, user_id=user).first()

        if not todo:
            return jsonify({"message": "Todo not found"}, 404)

        todo_json = request.get_json()
        print("todo_json", todo_json)

        if "task" in todo_json:
            todo.title = todo_json["task"]
        if "description" in todo_json:
            todo.description = todo_json["description"]

        # Use datetime.now() to get the current datetime
        todo.updated_at = datetime.datetime.utcnow()

        db.session.commit()
        serialized_todo = serialize_todo(todo)

        return (
            jsonify({"message": "Todo updated successfully", "todo": serialized_todo}),
            200,
        )
    except Exception as e:
        print("Error occurred", str(e))
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}, 500)
