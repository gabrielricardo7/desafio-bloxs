from apiflask import APIBlueprint, APIFlask
from .conta_route import bp as bp_conta

bp = APIBlueprint("", __name__, url_prefix="/")


def init_app(app: APIFlask):
    bp.register_blueprint(bp_conta)
    app.register_blueprint(bp)
