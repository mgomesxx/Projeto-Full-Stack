import random
from models.model import lista_usuarios, lista_codigos
from service.auth_service import gerar_codigo, enviar_whatsapp, gerar_token

def usuario(dados):
    for campo in ["nome", "cnpj", "email", "celular", "senha"]:
        if not dados.get(campo):
            return {"erro": f"{campo} é obrigatório"}
    if any(u["cnpj"] == dados["cnpj"] for u in lista_usuarios):
        return {"erro": "CNPJ já cadastrado"}

    dados["status"] = "Inativo"
    lista_usuarios.append(dados)

    codigo = gerar_codigo()
    lista_codigos.append({"cnpj": dados["cnpj"], "codigo": codigo})
    enviar_whatsapp(dados["celular"], codigo)

    return {"mensagem": "Cadastro realizado! Verifique seu WhatsApp para ativar a conta."}

def ativar_conta(cnpj, codigo):
    registro = next((c for c in lista_codigos if c["cnpj"] == cnpj), None)
    if not registro or registro["codigo"] != codigo:
        return {"erro": "Código inválido"}
    
    user = next((u for u in lista_usuarios if u["cnpj"] == cnpj), None)
    user["status"] = "Ativo"
    lista_codigos.remove(registro)
    return {"mensagem": "Conta ativada com sucesso!"}

def login(email, senha):
    user = next((u for u in lista_usuarios if u["email"] == email), None)
    if not user or user["senha"] != senha:
        return {"erro": "Email ou senha inválidos"}
    if user["status"] != "Ativo":
        return {"erro": "Conta não ativada"}
    token = gerar_token(email)
    return {"token": token}

def getUser(cnpj):
    user = next((u for u in lista_usuarios if u["cnpj"] == cnpj), None)
    return user or {"erro": "Usuário não encontrado"}

def deleteUser(cnpj):
    user = getUser(cnpj)
    if "erro" in user:
        return user
    lista_usuarios.remove(user)
    return {"mensagem": "Usuário deletado!"}

def editarUser(cnpj, dados):
    user = getUser(cnpj)
    if "erro" in user:
        return user
    if "nome" in dados:
        user["nome"] = dados["nome"]
    if "email" in dados:
        user["email"] = dados["email"]
    if "senha" in dados:
        user["senha"] = dados["senha"]
    if "celular" in dados:
        user["celular"] = dados["celular"]
    return {"mensagem": "Usuário atualizado!", "usuario": user}