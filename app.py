from flask import Flask, request, jsonify, render_template, send_from_directory
from controller.app import createUser
from controller.auth import ativarConta, loginVendedor, editarVendedor
from service.service import getUser, deleteUser, lista_usuarios
from controller.produto_controller import (
    criarProduto, listarProdutos, buscarProduto,
    editarProduto, inativarProduto, registrarVenda, verDashboard,
    ativarProduto, inativarVenda, listarVendas
)
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/imagens'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

@app.route('/upload', methods=['POST'])
def upload_imagem():
    if 'imagem' not in request.files:
        return jsonify({"erro": "Nenhum arquivo enviado"}), 400
    arquivo = request.files['imagem']
    if arquivo.filename == '':
        return jsonify({"erro": "Arquivo inválido"}), 400
    nome = secure_filename(arquivo.filename)
    arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nome))
    return jsonify({"imagem": nome}), 200

@app.route('/static/imagens/<nome>')
def ver_imagem(nome):
    return send_from_directory(app.config['UPLOAD_FOLDER'], nome)

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

@app.route('/produtos/<produto_id>/ativar', methods=['PUT'])
def reativarProduto(produto_id):
    return jsonify(ativarProduto(produto_id))

@app.route('/vendas', methods=['POST', 'GET'])
def vendas():
    if request.method == 'POST':
        return jsonify(registrarVenda())
    return jsonify(listarVendas())

@app.route('/vendas/<venda_id>/inativar', methods=['PUT'])
def desativarVenda(venda_id):
    return jsonify(inativarVenda(venda_id))

@app.route('/dashboard', methods=['GET'])
def verRelatorio():
    return jsonify(verDashboard())

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