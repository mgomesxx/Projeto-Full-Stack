from flask import request
from service.service import ativar_conta, login

def ativarConta():
    dados = request.get_json()
    return ativar_conta(dados["cnpj"], dados["codigo"])

def loginVendedor():
    dados = request.get_json()
    return login(dados["email"], dados["senha"])