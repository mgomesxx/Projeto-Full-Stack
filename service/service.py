from models.model import lista_usuarios

def usuario(dados_usuario):

    lista_usuarios.append(dados_usuario)

    return lista_usuarios


def getUser(cpf):

    for user in lista_usuarios:
        if user['cpf'] == cpf:
            return user
        
    return "Usuario nao encontrado!"


def deleteUser(cpf):

    usuario = getUser(cpf)

    for user in lista_usuarios:
        if user == usuario:
            lista_usuarios.remove(user)
            return "Usuario foi deletado!"
        
    return "Usuario nao foi encontrado!"