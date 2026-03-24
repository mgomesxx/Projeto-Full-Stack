from flask import Flask, request, jsonify
from controller.app import createUser
from controller.auth import ativarConta, loginVendedor
from service.service import getUser, deleteUser, lista_usuarios

app = Flask(__name__)

@app.route('/criar', methods=['POST'])
def criarUsuario():
    return jsonify(createUser())

@app.route('/ativar', methods=['POST'])
def ativar():
    return jsonify(ativarConta())

@app.route('/login', methods=['POST'])
def login():
    return jsonify(loginVendedor())

@app.route('/listar')
def listarUsuarios():
    return jsonify(lista_usuarios)

@app.route('/listar/<cnpj>')
def listarUsuario(cnpj):
    return jsonify(getUser(cnpj))

@app.route('/deletar/<cnpj>', methods=['DELETE'])
def deletarUsuario(cnpj):
    return jsonify(deleteUser(cnpj))

if __name__ == '__main__':
    app.run(debug=True)