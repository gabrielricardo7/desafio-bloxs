from apiflask import APIFlask

from app import routes
from app.configs import database, migrations


def create_app():
    app = APIFlask(__name__)

    database.init_app(app)
    migrations.init_app(app)
    routes.init_app(app)

    return app
