from app.models import Conta, Pessoa, Transacao


def procurar_conta(id_conta):
    conta: Conta = Conta.query.filter_by(id_conta=id_conta).first()

    return conta


def procurar_pessoa(id_pessoa):
    pessoa: Pessoa = Pessoa.query.filter_by(id_pessoa=id_pessoa).first()

    return pessoa


def procurar_transacoes(id_conta):
    transacoes: list[Transacao] = Transacao.query.filter_by(id_conta=id_conta).all()

    return transacoes
