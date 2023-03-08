from environs import Env
from apiflask import APIFlask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

env = Env()
env.read_env()
db = SQLAlchemy()
engine = create_engine(env("DB_URI"))


def init_app(app: APIFlask):
    app.config["JSON_SORT_KEYS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = env("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    app.db = db

    from app import models
