from apiflask import APIBlueprint

from app.controllers import conta_controller as control

bp = APIBlueprint("conta", __name__, url_prefix="/conta")

bp.post("/abrir")(control.criar_conta)
bp.post("/deposito/<int:id_conta>")(control.depositar)
bp.get("/saldo/<int:id_conta>")(control.consultar_saldo)
bp.post("/saque/<int:id_conta>")(control.sacar)
bp.post("/bloqueio/<int:id_conta>")(control.bloquear_conta)
bp.get("/extrato/<int:id_conta>")(control.recuperar_extrato)
