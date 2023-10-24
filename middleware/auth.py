from functools import wraps
import jwt, datetime
import settings
from flask import request, jsonify
from user_authentication.models import User

secret_key = settings.secret_key


def auth_token(existing_user):
    payload = {
        "user_id": existing_user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
    }
    return jwt.encode(payload, secret_key, algorithm="HS256")


def authenticate_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"msg": "Unauthorized"}), 401

        token = token.split(" ")[-1]

        try:
            decoded_token = jwt.decode(token, secret_key, algorithms=["HS256"])
            user_id = decoded_token.get("user_id")
            user = User.query.filter_by(id=user_id).first()

            if not user:
                return jsonify({"msg": "Unauthorized"}), 401
            print("user_id", user_id)
            return f(user_id, *args, **kwargs)

        except jwt.ExpiredSignatureError:
            return jsonify({"msg": "Token has expired"}), 401

        except jwt.InvalidTokenError:
            return jsonify({"msg": "Invalid token"}), 401

    return decorated_function
