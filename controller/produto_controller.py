from flask import request
from service.auth_service import verificar_token
from service.produto_service import (
    cadastrar_produto, listar_produtos, buscar_produto,
    editar_produto, inativar_produto, registrar_venda, dashboard,
    ativar_produto, inativar_venda, listar_vendas
)

def get_cnpj_do_token():
    from models.model import lista_usuarios
    token = request.headers.get("Authorization")
    if not token:
        return None, {"erro": "Token não fornecido"}
    resultado = verificar_token(token)
    if "erro" in resultado:
        return None, resultado
    email = resultado["email"]
    user = next((u for u in lista_usuarios if u["email"] == email), None)
    if not user:
        return None, {"erro": "Usuário não encontrado"}
    return user["cnpj"], None

def criarProduto():
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return cadastrar_produto(cnpj, request.get_json())

def listarProdutos():
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return listar_produtos(cnpj)

def buscarProduto(produto_id):
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return buscar_produto(produto_id, cnpj)

def editarProduto(produto_id):
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return editar_produto(produto_id, cnpj, request.get_json())

def ativarProduto(produto_id):
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return ativar_produto(produto_id, cnpj)

def inativarProduto(produto_id):
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return inativar_produto(produto_id, cnpj)

def registrarVenda():
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return registrar_venda(cnpj, request.get_json())

def inativarVenda(venda_id):
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return inativar_venda(venda_id, cnpj)

def listarVendas():
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return listar_vendas(cnpj)

def verDashboard():
    cnpj, erro = get_cnpj_do_token()
    if erro:
        return erro
    return dashboard(cnpj)