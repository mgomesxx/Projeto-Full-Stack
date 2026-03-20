from models.model import lista_usuarios

def usuario(dados_usuario):
    for campo in ["nome", "email", "senha", "cpf"]:
        if not dados_usuario.get(campo):
            return {"erro": f"{campo} é obrigatório"}
    if any(u["cpf"] == dados_usuario["cpf"] for u in lista_usuarios):
        return {"erro": "CPF já cadastrado"}
    lista_usuarios.append(dados_usuario)
    return {"mensagem": "Usuário criado!", "usuario": dados_usuario}

def getUser(cpf):
    for user in lista_usuarios:
        if user["cpf"] == cpf:
            return user
    return {"erro": "Usuário não encontrado"}

def deleteUser(cpf):
    user = getUser(cpf)
    if "erro" in user:
        return user
    lista_usuarios.remove(user)
    return {"mensagem": "Usuário deletado!"}