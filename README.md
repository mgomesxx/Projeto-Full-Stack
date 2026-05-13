# 🛒 Meu Mercadinho — Sistema de Gestão de Estoque

Sistema full stack desenvolvido em Python com Flask para gerenciamento de mini mercados, com autenticação via JWT, ativação de conta por WhatsApp e interface web completa.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** — framework web
- **PyJWT** — autenticação com tokens JWT
- **Twilio** — envio de código de ativação via WhatsApp
- **python-dotenv** — gerenciamento de variáveis de ambiente
- **Werkzeug** — upload de imagens
- **HTML + CSS + JavaScript** — interface web

---

## 📁 Estrutura de Pastas

```
Projeto-Full-Stack/
├── app.py                              # Entry point da aplicação
├── .env                                # Variáveis de ambiente (não sobe pro GitHub)
├── .gitignore
├── static/
│   └── imagens/                        # Imagens dos produtos
├── templates/
│   ├── cadastro.html                   # Tela de cadastro de seller
│   ├── ativacao.html                   # Tela de ativação de conta
│   ├── login.html                      # Tela de login
│   ├── produtos.html                   # Catálogo de produtos
│   ├── cadastro_produto.html           # Tela de cadastro de produto
│   ├── editar_produto.html             # Tela de edição de produto
│   ├── vendas.html                     # Tela de vendas
│   └── dashboard.html                  # Painel de relatórios
├── controller/
│   ├── app.py                          # Lógica de criação de usuário
│   ├── auth.py                         # Lógica de ativação, login e edição
│   └── produto_controller.py           # Lógica de produtos e vendas
├── models/
│   └── model.py                        # Armazenamento em memória
└── service/
    ├── service.py                      # Regras de negócio dos sellers
    ├── auth_service.py                 # JWT e integração Twilio
    └── produto_service.py              # Regras de negócio de produtos e vendas
```

---

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```
TWILIO_SID=seu_account_sid
TWILIO_TOKEN=seu_auth_token
SECRET_KEY=sua_chave_secreta
```

---

## ▶️ Como Executar

```bash
pip install flask pyjwt twilio python-dotenv werkzeug
python app.py
```

Acesse no navegador:
```
http://127.0.0.1:5000/pagina/cadastro
```

---

## 🔌 Rotas da API

### Sellers
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/criar` | Cadastra um novo seller |
| POST | `/ativar` | Ativa a conta com o código do WhatsApp |
| POST | `/login` | Autentica e retorna o token JWT |
| GET | `/listar` | Lista todos os sellers |
| GET | `/listar/<cnpj>` | Busca um seller pelo CNPJ |
| PUT | `/editar/<cnpj>` | Edita informações do seller |
| DELETE | `/deletar/<cnpj>` | Remove um seller |

### Produtos
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/produtos` | Cadastra um produto |
| GET | `/produtos` | Lista produtos do seller |
| GET | `/produtos/<id>` | Busca um produto |
| PUT | `/produtos/<id>` | Edita um produto |
| PUT | `/produtos/<id>/ativar` | Ativa um produto |
| PUT | `/produtos/<id>/inativar` | Inativa um produto |
| POST | `/upload` | Faz upload de imagem |

### Vendas e Dashboard
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/vendas` | Registra uma venda |
| GET | `/dashboard` | Retorna relatório de vendas e estoque |

### Telas
| Rota | Descrição |
|------|-----------|
| `/pagina/cadastro` | Tela de cadastro |
| `/pagina/ativacao` | Tela de ativação |
| `/pagina/login` | Tela de login |
| `/pagina/produtos` | Catálogo de produtos |
| `/pagina/cadastro_produto` | Cadastro de produto |
| `/pagina/editar_produto` | Edição de produto |
| `/pagina/vendas` | Registro de vendas |
| `/pagina/dashboard` | Painel de relatórios |

---

## 🔐 Autenticação

Todas as rotas de produtos e vendas exigem o token JWT no header:

```
Authorization: seu_token_aqui
```

---

## 📋 Fluxo do Sistema

1. Seller se cadastra → recebe código no WhatsApp
2. Seller ativa a conta com o código
3. Seller faz login → recebe token JWT
4. Seller gerencia produtos (cadastrar, editar, ativar, inativar)
5. Seller registra vendas
6. Seller visualiza relatórios no dashboard
