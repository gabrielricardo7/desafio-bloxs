from http import HTTPStatus

from app.models import Pessoa


def listar_pessoas():
    pessoas: list[Pessoa] = Pessoa.query.all()

    lista = []

    for p in pessoas:
        x = {
            "idPessoa": p.id_pessoa,
            "nome": p.nome,
            "cpf": p.cpf,
            "dataNascimento": p.data_nascimento,
        }
        lista.append(x)

    return lista, HTTPStatus.OK
