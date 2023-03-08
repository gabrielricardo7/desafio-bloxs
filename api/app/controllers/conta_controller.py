from datetime import date
from http import HTTPStatus

from flask import request

from app.configs.database import db
from app.models import Conta, Transacao


def criar_conta():
    req = request.get_json()

    conta = Conta(
        id_pessoa=req["idPessoa"],
        saldo=req["saldo"],
        limite_saque_diario=req["limiteSaqueDiario"],
        tipo_conta=req["tipoConta"],
    )

    db.session.add(conta)
    db.session.commit()

    nova_conta = {
        "idConta": conta.id_conta,
        "idPessoa": conta.id_pessoa,
        "saldo": conta.saldo,
        "limiteSaqueDiario": conta.limite_saque_diario,
        "flagAtivo": conta.flag_ativo,
        "tipoConta": conta.tipo_conta,
        "dataCriacao": conta.data_criacao,
    }

    return nova_conta, HTTPStatus.CREATED


def depositar(id_conta: int):
    conta: Conta = Conta.query.filter_by(id_conta=id_conta).first()

    if not conta:
        return {"msg": "conta não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == False:
        return {"msg": f"conta {conta.id_conta} bloqueada!"}

    req = request.get_json()

    if not req:
        return {}, HTTPStatus.NO_CONTENT

    valor = req["valor"]

    if valor <= 0:
        return {"msg": "valor deve ser positivo"}, HTTPStatus.NOT_ACCEPTABLE

    conta.saldo += valor

    db.session.commit()

    transacao = Transacao(
        id_conta=id_conta,
        valor=valor,
        deposito=True,
    )

    db.session.add(transacao)
    db.session.commit()

    nova_transacao = {
        "idTransacao": transacao.id_transacao,
        "idConta": transacao.id_conta,
        "valor": transacao.valor,
        "dataTransacao": transacao.data_transacao,
        "tipo": "deposito" if transacao.deposito else "saque",
    }

    return nova_transacao, HTTPStatus.OK


def consultar_saldo(id_conta: int):
    conta: Conta = Conta.query.filter_by(id_conta=id_conta).first()

    if not conta:
        return {"msg": "conta não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == False:
        return {"msg": f"conta {conta.id_conta} bloqueada!"}

    saldo = conta.saldo

    return {"saldo": saldo}


def sacar(id_conta: int):
    conta: Conta = Conta.query.filter_by(id_conta=id_conta).first()

    if not conta:
        return {"msg": "conta não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == False:
        return {"msg": f"conta {conta.id_conta} bloqueada!"}

    req = request.get_json()

    if not req:
        return {}, HTTPStatus.NO_CONTENT

    valor = req["valor"]

    if valor <= 0:
        return {"msg": "valor deve ser positivo"}, HTTPStatus.NOT_ACCEPTABLE

    limite = conta.limite_saque_diario

    transacoes: list[Transacao] = Transacao.query.filter_by(id_conta=id_conta).all()

    saques: list[Transacao] = []

    for transacao in transacoes:
        if not transacao.deposito:
            saques.append(transacao)

    soma = 0

    for x in saques:
        if x.data_transacao[:10] == str(date.today()):
            soma += x.valor

    if not limite > (soma + valor):
        return {"msg": "limite de saque diário atingido!"}

    conta.saldo -= valor

    db.session.commit()

    t = Transacao(
        id_conta=id_conta,
        valor=valor,
        deposito=False,
    )

    db.session.add(transacao)
    db.session.commit()

    nova_transacao = {
        "idTransacao": t.id_transacao,
        "idConta": t.id_conta,
        "valor": t.valor,
        "dataTransacao": t.data_transacao,
        "tipo": "deposito" if t.deposito else "saque",
    }

    return nova_transacao, HTTPStatus.OK


def bloquear_conta(id_conta: int):
    conta: Conta = Conta.query.filter_by(id_conta=id_conta).first()

    if not conta:
        return {"msg": "conta não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == True:
        conta.flag_ativo = False

        db.session.commit()

    return {"msg": f"conta {conta.id_conta} bloqueada!"}, HTTPStatus.OK


def recuperar_extrato(id_conta: int):
    transacoes: list[Transacao] = Transacao.query.filter_by(id_conta=id_conta).all()

    extrato = []

    for transacao in transacoes:
        extrato.append(
            {
                "idTransacao": transacao.id_transacao,
                "idConta": transacao.id_conta,
                "valor": transacao.valor,
                "dataTransacao": transacao.data_transacao,
                "tipo": "deposito" if transacao.deposito else "saque",
            }
        )

    return {"extrato": extrato}, HTTPStatus.OK
