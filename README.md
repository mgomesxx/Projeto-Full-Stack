# Projeto Full Stack — API gestão de estoque para mini mercado

API REST desenvolvida em Python com Flask para gerenciamento de mini mercados (vendedores), com autenticação via JWT e ativação de conta por WhatsApp usando Twilio.

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** — framework web
- **PyJWT** — autenticação com tokens JWT
- **Twilio** — envio de código de ativação via WhatsApp
- **python-dotenv** — gerenciamento de variáveis de ambiente

## 📁 Estrutura de Pastas

```
Projeto-Full-Stack/
├── app.py                          # Entry point da aplicação
├── .env                            # Variáveis de ambiente (não sobe pro GitHub)
├── .gitignore
├── controller/
│   ├── app.py                      # Lógica de criação de usuário
│   └── auth.py                     # Lógica de ativação e login
├── models/
│   └── model.py                    # Armazenamento em memória
└── service/
    ├── service.py                  # Regras de negócio
    └── auth_service.py             # JWT e integração Twilio
```

## ⚙️ Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```
TWILIO_SID=seu_account_sid
TWILIO_TOKEN=seu_auth_token
SECRET_KEY=sua_chave_secreta
```

## 🔌 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/criar` | Cadastra um novo vendedor |
| POST | `/ativar` | Ativa a conta com o código recebido via WhatsApp |
| POST | `/login` | Autentica o vendedor e retorna o token JWT |
| GET | `/listar` | Lista todos os vendedores |
| GET | `/listar/<cnpj>` | Busca um vendedor pelo CNPJ |
| DELETE | `/deletar/<cnpj>` | Remove um vendedor |
