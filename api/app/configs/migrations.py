from apiflask import APIFlask
from flask_migrate import Migrate


def init_app(app: APIFlask):
    Migrate(app=app, db=app.db, compare_type=True)
