from flask import request
from service.service import ativar_conta, login, editarUser
from service.auth_service import verificar_token

def ativarConta():
    dados = request.get_json()
    return ativar_conta(dados["cnpj"], dados["codigo"])

def loginVendedor():
    dados = request.get_json()
    return login(dados["email"], dados["senha"])

def editarVendedor(cnpj):
    token = request.headers.get("Authorization")
    if not token:
        return {"erro": "Token não fornecido"}
    resultado = verificar_token(token)
    if "erro" in resultado:
        return resultado
    dados = request.get_json()
    return editarUser(cnpj, dados)