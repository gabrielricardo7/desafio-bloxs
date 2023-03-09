from datetime import date
from http import HTTPStatus

from flask import request

from app.configs.database import db
from app.models import Conta, Transacao
from app.utils import procurar_conta, procurar_pessoa, procurar_transacoes


def criar_conta():
    req = request.get_json()

    id_pessoa = req["idPessoa"] if req["idPessoa"] else None

    if id_pessoa is None:
        return {"msg": "id não informado."}

    pessoa = procurar_pessoa(id_pessoa)

    if not pessoa:
        return {"msg": "pessoa não encontrada."}

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
        "pessoa": {
            "idPessoa": pessoa.id_pessoa,
            "nome": pessoa.nome,
            "cpf": pessoa.cpf,
            "dataNascimento": pessoa.data_nascimento,
        },
        "saldo": conta.saldo,
        "limiteSaqueDiario": conta.limite_saque_diario,
        "flagAtivo": conta.flag_ativo,
        "tipoConta": conta.tipo_conta,
        "dataCriacao": conta.data_criacao,
    }

    return nova_conta, HTTPStatus.CREATED


def depositar(id_conta: int):
    conta = procurar_conta(id_conta)

    if not conta:
        return {"msg": f"conta {id_conta} não encontrada!"}, HTTPStatus.NOT_FOUND

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
        "valor": transacao.valor,
        "dataTransacao": transacao.data_transacao,
        "tipo": "deposito" if transacao.deposito else "saque",
        "idConta": transacao.id_conta,
    }

    return nova_transacao, HTTPStatus.OK


def consultar_saldo(id_conta: int):
    conta = procurar_conta(id_conta)

    if not conta:
        return {"msg": f"conta {id_conta} não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == False:
        return {"msg": f"conta {conta.id_conta} bloqueada!"}

    saldo = conta.saldo

    return {"saldo": saldo}


def sacar(id_conta: int):
    conta = procurar_conta(id_conta)

    if not conta:
        return {"msg": f"conta {id_conta} não encontrada!"}, HTTPStatus.NOT_FOUND

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

    for t in transacoes:
        if not t.deposito:
            saques.append(t)

    soma = 0

    for x in saques:
        if x.data_transacao.date() == date.today():
            soma += x.valor

    if limite <= soma:
        return {"msg": "limite de saque diário atingido!"}

    if limite < (soma + valor):
        return {
            "msg": f"acima do limite de saque diário! - Disponível: {(limite - soma)}"
        }

    conta.saldo -= valor

    db.session.commit()

    transacao = Transacao(
        id_conta=id_conta,
        valor=valor,
        deposito=False,
    )

    db.session.add(transacao)
    db.session.commit()

    nova_transacao = {
        "idTransacao": transacao.id_transacao,
        "valor": transacao.valor,
        "dataTransacao": transacao.data_transacao,
        "tipo": "deposito" if transacao.deposito else "saque",
        "idConta": transacao.id_conta,
    }

    return nova_transacao, HTTPStatus.OK


def bloquear_conta(id_conta: int):
    conta = procurar_conta(id_conta)

    if not conta:
        return {"msg": f"conta {id_conta} não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == True:
        conta.flag_ativo = False

        db.session.commit()

    return {"msg": f"conta {conta.id_conta} bloqueada!"}, HTTPStatus.OK


def recuperar_extrato(id_conta: int):
    conta = procurar_conta(id_conta)

    if not conta:
        return {"msg": f"conta {id_conta} não encontrada!"}, HTTPStatus.NOT_FOUND

    if conta.flag_ativo == False:
        return {"msg": f"conta {conta.id_conta} bloqueada!"}

    pessoa = procurar_pessoa(conta.id_pessoa)

    x = {
        "idConta": conta.id_conta,
        "idPessoa": pessoa.id_pessoa,
        "nome": pessoa.nome,
        "cpf": pessoa.cpf,
        "dataNascimento": pessoa.data_nascimento,
    }

    transacoes = procurar_transacoes(id_conta)

    extrato = []

    for transacao in transacoes:
        extrato.append(
            {
                "idTransacao": transacao.id_transacao,
                "valor": transacao.valor,
                "dataTransacao": transacao.data_transacao,
                "tipo": "deposito" if transacao.deposito else "saque",
            }
        )

    x["extrato"] = extrato

    return x, HTTPStatus.OK
