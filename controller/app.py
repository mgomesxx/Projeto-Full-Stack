from flask import request
from service.service import usuario


def createUser():

    dados_usuario = request.get_json()

    lista_usuarios = usuario(dados_usuario)

    return lista_usuarios