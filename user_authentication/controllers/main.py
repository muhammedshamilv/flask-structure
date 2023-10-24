import datetime
from logging import Logger
from tokenize import generate_tokens
from flask import current_app, render_template, views, jsonify, request
import jwt

from app import db
from middleware.auth import auth_token
from user_authentication.models import User
from user_authentication.serializer import serialize_user


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
        existing_user = User.query.filter_by(username=user_json["username"]).first()
        user_data = serialize_user(existing_user)
        token = auth_token(existing_user)
        print("user_data", token)
        return (
            jsonify(
                {
                    "message": "Login successful",
                    "token": token,
                    "user": user_data,
                }
            ),
            201,
        )

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
            user_data = serialize_user(existing_user)
            token = auth_token(existing_user)
            return (
                jsonify(
                    {
                        "message": "Login successful",
                        "token": token,
                        "user": user_data,
                    }
                ),
                200,
            )
    except Exception as e:
        Logger.error("An error occurred: %s" % e)
        return jsonify({"message": f"An error occurred {e}"}), 500
