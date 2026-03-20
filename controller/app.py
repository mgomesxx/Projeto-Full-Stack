from flask import request
from service.service import usuario

def createUser():
    dados_usuario = request.get_json()
    return usuario(dados_usuario)