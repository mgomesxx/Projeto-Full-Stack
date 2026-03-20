from flask import Flask, request, jsonify
from controller.app import createUser
from service.service import getUser, deleteUser, lista_usuarios

app = Flask(__name__)

@app.route('/criar', methods=['POST'])
def criarUsuario():
    return jsonify(createUser())

@app.route('/listar')
def listarUsuarios():
    return jsonify(lista_usuarios)

@app.route('/listar/<cpf>')
def listarUsuario(cpf):
    return jsonify(getUser(cpf))

@app.route('/deletar/<cpf>', methods=['DELETE'])
def deletarUsuario(cpf):
    return jsonify(deleteUser(cpf))

if __name__ == '__main__':
    app.run(debug=True)