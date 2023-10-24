from logging import Logger
from tokenize import generate_tokens
from flask import current_app, render_template, views, jsonify, request

from app import db
from user_authentication.models import User


class HealthCheck(views.MethodView):
    def get(self):
        return jsonify({"msg": "health ok"}), 200


def login_template():
    return render_template("login.html")


def signup_template():
    return render_template("signup.html")


def home_template():
    return render_template("home.html")


def create_user():
    try:
        user_json = request.get_json()
        new_user = User(username=user_json["username"])
        new_user.set_password(user_json["password"])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "user added successfully"}), 201

    except Exception as e:
        Logger.error(e)
        return jsonify({"message": f"An error occurred {e}"}), 500


def login():
    try:
        user_json = request.get_json()
        existing_user = User.query.filter_by(username=user_json["username"]).first()

        if not existing_user or not existing_user.check_password(user_json["password"]):
            return jsonify({"message": "Invalid username/password combination"}), 403
        else:
            # You can generate an authentication token here if needed
            return jsonify({"message": "Login successful"}), 200
    except Exception as e:
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}), 500
