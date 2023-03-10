from apiflask import APIBlueprint

from app.controllers import pessoa_controller as control

bp = APIBlueprint("pessoa", __name__, url_prefix="/pessoa")

bp.get("")(control.listar_pessoas)
