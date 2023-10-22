from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import settings

database = settings.database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database
db = SQLAlchemy(app)

migrate = Migrate(app, db)


from base_app.urls import health_check_bp

app.register_blueprint(health_check_bp)
