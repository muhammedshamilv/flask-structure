from flask import Flask, Response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import settings

database = settings.database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database
db = SQLAlchemy(app)
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_basicauth import BasicAuth

from werkzeug.exceptions import HTTPException

migrate = Migrate(app, db)

app.config["FLASK_ADMIN_SWATCH"] = "cerulean"
app.config["BASIC_AUTH_USERNAME"] = settings.username
app.config["BASIC_AUTH_PASSWORD"] = settings.password

basic_auth = BasicAuth(app)

from todo.models import Todo
from user_authentication.models import User


class AuthException(HTTPException):
    def __init__(self, message):
        super().__init__(
            message,
            Response(
                "You could not be authenticated. Please refresh the page.",
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            ),
        )


class SecureModelView(ModelView):
    def is_accessible(self):
        if not basic_auth.authenticate():
            raise AuthException("Not authenticated.")
        else:
            return True

    def inaccessible_callback(self, name, **kwargs):
        return redirect(basic_auth.challenge())


admin = Admin(app, name="Admin Panel", template_mode="bootstrap3")

admin.add_view(SecureModelView(User, db.session, name="user"))
admin.add_view(SecureModelView(Todo, db.session, name="todo"))


from user_authentication.urls import health_check_bp, login_bp
from todo.urls import todo_bp

app.register_blueprint(health_check_bp)
app.register_blueprint(login_bp)
app.register_blueprint(todo_bp)


# logs
# newrelic
# swagger
# pytest
