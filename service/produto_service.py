from models.model import lista_produtos, lista_vendas
import uuid

def cadastrar_produto(cnpj_seller, dados):
    for campo in ["nome", "preco", "quantidade", "imagem"]:
        if not dados.get(campo):
            return {"erro": f"{campo} é obrigatório"}
    produto = {
        "id": str(uuid.uuid4()),
        "cnpj_seller": cnpj_seller,
        "nome": dados["nome"],
        "preco": dados["preco"],
        "quantidade": dados["quantidade"],
        "imagem": dados["imagem"],
        "status": "Ativo"
    }
    lista_produtos.append(produto)
    return {"mensagem": "Produto cadastrado!", "produto": produto}

def listar_produtos(cnpj_seller):
    return [p for p in lista_produtos if p["cnpj_seller"] == cnpj_seller]

def buscar_produto(produto_id, cnpj_seller):
    p = next((p for p in lista_produtos if p["id"] == produto_id and p["cnpj_seller"] == cnpj_seller), None)
    return p or {"erro": "Produto não encontrado"}

def editar_produto(produto_id, cnpj_seller, dados):
    p = buscar_produto(produto_id, cnpj_seller)
    if "erro" in p:
        return p
    for campo in ["nome", "preco", "quantidade", "imagem"]:
        if campo in dados:
            p[campo] = dados[campo]
    return {"mensagem": "Produto atualizado!", "produto": p}

def inativar_produto(produto_id, cnpj_seller):
    p = buscar_produto(produto_id, cnpj_seller)
    if "erro" in p:
        return p
    p["status"] = "Inativo"
    return {"mensagem": "Produto inativado!"}

def ativar_produto(produto_id, cnpj_seller):
    p = buscar_produto(produto_id, cnpj_seller)
    if "erro" in p:
        return p
    p["status"] = "Ativo"
    return {"mensagem": "Produto ativado!"}

def registrar_venda(cnpj_seller, dados):
    from models.model import lista_usuarios
    seller = next((u for u in lista_usuarios if u["cnpj"] == cnpj_seller), None)
    if not seller or seller["status"] != "Ativo":
        return {"erro": "Seller inativo não pode realizar vendas"}

    p = next((p for p in lista_produtos if p["id"] == dados.get("produto_id") and p["cnpj_seller"] == cnpj_seller), None)
    if not p:
        return {"erro": "Produto não encontrado"}
    if p["status"] == "Inativo":
        return {"erro": "Produto inativo não pode ser vendido"}
    if dados.get("quantidade", 0) > p["quantidade"]:
        return {"erro": "Quantidade insuficiente em estoque"}

    quantidade = dados["quantidade"]

    if quantidade >= 10:
        desconto = 0.10
    elif quantidade >= 5:
        desconto = 0.05
    else:
        desconto = 0.0

    total_sem_desconto = p["preco"] * quantidade
    total_com_desconto = total_sem_desconto * (1 - desconto)

    p["quantidade"] -= quantidade

    venda = {
        "id": str(uuid.uuid4()),
        "cnpj_seller": cnpj_seller,
        "produto_id": p["id"],
        "nome_produto": p["nome"],
        "quantidade": quantidade,
        "preco_unitario": p["preco"],
        "desconto": f"{int(desconto * 100)}%",
        "total": round(total_com_desconto, 2),
        "status": "Ativo"
    }
    lista_vendas.append(venda)
    return {"mensagem": "Venda registrada!", "venda": venda}

def inativar_venda(venda_id, cnpj_seller):
    venda = next((v for v in lista_vendas if v["id"] == venda_id and v["cnpj_seller"] == cnpj_seller), None)
    if not venda:
        return {"erro": "Venda não encontrada"}
    if venda.get("status") == "Inativo":
        return {"erro": "Venda já inativada"}
    produto = next((p for p in lista_produtos if p["id"] == venda["produto_id"]), None)
    if produto:
        produto["quantidade"] += venda["quantidade"]
    venda["status"] = "Inativo"
    return {"mensagem": "Venda inativada e estoque devolvido!"}

def listar_vendas(cnpj_seller):
    return [v for v in lista_vendas if v["cnpj_seller"] == cnpj_seller and v.get("status") != "Inativo"]

def dashboard(cnpj_seller):
    produtos = listar_produtos(cnpj_seller)
    vendas = listar_vendas(cnpj_seller)
    return {
        "quantidade_produtos_estoque": sum(p["quantidade"] for p in produtos),
        "valor_total_vendido": sum(v["total"] for v in vendas),
        "total_vendas": len(vendas),
        "vendas": vendas
    }