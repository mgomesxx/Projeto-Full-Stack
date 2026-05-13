from flask import Flask, request, jsonify
from controller.app import createUser
from controller.auth import ativarConta, loginVendedor, editarVendedor
from service.service import getUser, deleteUser, lista_usuarios
from flask import render_template
from controller.produto_controller import (
    criarProduto, listarProdutos, buscarProduto,
    editarProduto, inativarProduto, registrarVenda, verDashboard
)

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

@app.route('/editar/<cnpj>', methods=['PUT'])
def editarUsuario(cnpj):
    return jsonify(editarVendedor(cnpj))

@app.route('/deletar/<cnpj>', methods=['DELETE'])
def deletarUsuario(cnpj):
    return jsonify(deleteUser(cnpj))

@app.route('/produtos', methods=['POST'])
def novoProduto():
    return jsonify(criarProduto())

@app.route('/produtos', methods=['GET'])
def listarMeusProdutos():
    return jsonify(listarProdutos())

@app.route('/produtos/<produto_id>', methods=['GET'])
def detalhesProduto(produto_id):
    return jsonify(buscarProduto(produto_id))

@app.route('/produtos/<produto_id>', methods=['PUT'])
def atualizarProduto(produto_id):
    return jsonify(editarProduto(produto_id))

@app.route('/produtos/<produto_id>/inativar', methods=['PUT'])
def desativarProduto(produto_id):
    return jsonify(inativarProduto(produto_id))

@app.route('/vendas', methods=['POST'])
def novaVenda():
    return jsonify(registrarVenda())

@app.route('/dashboard', methods=['GET'])
def verRelatorio():
    return jsonify(verDashboard())

    from flask import render_template

@app.route('/pagina/cadastro')
def pagina_cadastro():
    return render_template('cadastro.html')

@app.route('/pagina/ativacao')
def pagina_ativacao():
    return render_template('ativacao.html')

@app.route('/pagina/login')
def pagina_login():
    return render_template('login.html')

@app.route('/pagina/produtos')
def pagina_produtos():
    return render_template('produtos.html')

@app.route('/pagina/cadastro_produto')
def pagina_cadastro_produto():
    return render_template('cadastro_produto.html')

@app.route('/pagina/editar_produto')
def pagina_editar_produto():
    return render_template('editar_produto.html')

@app.route('/pagina/vendas')
def pagina_vendas():
    return render_template('vendas.html')

@app.route('/pagina/dashboard')
def pagina_dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/pagina/cadastro')
def pagina_cadastro():
    return render_template('cadastro.html')

@app.route('/pagina/ativacao')
def pagina_ativacao():
    return render_template('ativacao.html')

@app.route('/pagina/login')
def pagina_login():
    return render_template('login.html')

@app.route('/pagina/produtos')
def pagina_produtos():
    return render_template('produtos.html')