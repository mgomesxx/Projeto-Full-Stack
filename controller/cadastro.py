from flask import Flask, request, jsonify
import random
import sqlite3

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    nome = data['nome']
    cnpj = data['cnpj']
    email = data['email']
    celular = data['celular']
    senha = data['senha']
    status = 'Inativo'