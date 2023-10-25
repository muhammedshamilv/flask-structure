from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import settings

database = settings.database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database
db = SQLAlchemy(app)

migrate = Migrate(app, db)


from user_authentication.urls import health_check_bp, login_bp

from todo.urls import todo_bp

app.register_blueprint(health_check_bp)
app.register_blueprint(login_bp)
app.register_blueprint(todo_bp)


# admin
# logs
# newrelic
# swagger
# pytest
