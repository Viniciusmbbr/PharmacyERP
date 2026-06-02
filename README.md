# 🏥 PharmacyERP

Sistema de Gestão para Farmácias construído com **FastAPI**, **SQLAlchemy 2.0** e **WebSocket** em tempo real.

> Projeto acadêmico com arquitetura limpa (Domain-Driven Design), autenticação JWT, conformidade farmacêutica FEFO e dashboard ao vivo.

---

## ✨ Funcionalidades

| Módulo | Descrição |
|---|---|
| 🔐 Autenticação | Login/registro com JWT e 4 níveis de acesso (roles) |
| 💊 Medicamentos | CRUD completo com código EAN, preço de custo/venda |
| 📦 Lotes | Controle de lotes com data de validade e rastreabilidade |
| 🛒 Vendas | Fluxo completo com seleção automática FEFO |
| 🚚 Compras | Gerenciamento de pedidos a fornecedores |
| 🏢 Fornecedores | Cadastro e histórico de compras |
| 🔔 Alertas | Notificações de estoque baixo e medicamentos próximos do vencimento |
| 📊 Relatórios | Dashboard com KPIs e métricas em tempo real |
| ⚡ WebSocket | Atualizações ao vivo sem necessidade de refresh |

---

## 🛠️ Stack Tecnológica

- **Backend:** [FastAPI 0.104](https://fastapi.tiangolo.com/) + Python 3.10
- **ORM:** [SQLAlchemy 2.0](https://docs.sqlalchemy.org/) com Mapped types
- **Banco de dados:** SQLite (dev) / PostgreSQL (produção)
- **Migrações:** [Alembic](https://alembic.sqlalchemy.org/)
- **Validação:** [Pydantic v2](https://docs.pydantic.dev/)
- **Autenticação:** JWT via `python-jose` + `bcrypt`
- **WebSocket:** Nativo FastAPI
- **Testes:** Pytest + HTTPX
- **Containers:** Docker + Docker Compose

---

## 📁 Estrutura do Projeto

```
ERPPharmacy/
├── API/
│   ├── main.py              # Aplicação FastAPI (entry point)
│   ├── schemas.py           # Schemas Pydantic (request/response)
│   ├── exceptions.py        # Exceções customizadas
│   ├── middleware.py        # Middleware de autenticação JWT
│   ├── routes/              # Routers por domínio
│   │   ├── auth_routes.py
│   │   ├── medicamentos.py
│   │   ├── lotes.py
│   │   ├── vendas.py
│   │   ├── compras.py
│   │   ├── fornecedores.py
│   │   ├── alertas.py
│   │   ├── relatorios.py
│   │   └── websocket_routes.py
│   ├── websocket/           # Gerenciador de conexões WebSocket
│   ├── index.html           # Dashboard principal
│   ├── vendas.html          # Página de vendas
│   ├── estoque.html         # Página de estoque
│   ├── script.js            # Helpers de fetch e WebSocket
│   └── Style.css
│
├── Application/
│   └── services/            # Lógica de negócio
│       ├── auth_service.py
│       ├── medicamento_service.py
│       ├── venda_service.py  # Inclui algoritmo FEFO
│       ├── compra_service.py
│       ├── lote_service.py
│       ├── fornecedor_service.py
│       ├── alerta_service.py
│       └── relatorio_service.py
│
├── Domain/                  # Modelos ORM (entidades)
│   ├── Medicamento.py
│   ├── Lote.py
│   ├── Venda.py             # Venda + VendaItem (com lote_id FEFO)
│   ├── Compra.py
│   ├── Fornecedor.py
│   ├── Usuario.py
│   ├── Alerta.py
│   └── Enums/
│
├── Infrastructure/
│   ├── database.py          # Configuração do SQLAlchemy
│   ├── seeds.py             # Dados iniciais de exemplo
│   └── logger.py
│
├── migrations/              # Alembic migrations
├── tests/                   # Testes automatizados (10 testes)
├── config.py                # Configurações centralizadas
├── setup_database.py        # Script de inicialização do banco
├── docker-compose.yml
├── Dockerfile
└── Requirements.txt
```

---

## 🚀 Como Rodar

Veja o guia completo em **[COMO_RODAR.md](./COMO_RODAR.md)**.

### Início rápido (3 comandos)

```bash
pip install -r Requirements.txt
python setup_database.py
uvicorn API.main:app --reload
```

Acesse: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔐 Credenciais Padrão

| Campo | Valor |
|---|---|
| Email | `admin@pharmacy.com` |
| Senha | `Admin123!` |

---

## 🐳 Rodando com Docker

```bash
# Subir API + PostgreSQL + pgAdmin
docker-compose up

# Em background
docker-compose up -d
```

| Serviço | URL |
|---|---|
| API | http://localhost:8000 |
| Docs interativos | http://localhost:8000/docs |
| pgAdmin | http://localhost:5050 |

---

## 📡 Endpoints Principais

### Auth
| Método | Rota | Descrição |
|---|---|---|
| POST | `/auth/register` | Registrar novo usuário |
| POST | `/auth/login` | Login e geração de token JWT |

### Medicamentos
| Método | Rota | Descrição |
|---|---|---|
| GET | `/medicamentos` | Listar medicamentos (paginado) |
| POST | `/medicamentos` | Cadastrar medicamento |
| GET | `/medicamentos/{id}` | Buscar por ID |
| PUT | `/medicamentos/{id}` | Atualizar |
| DELETE | `/medicamentos/{id}` | Remover |

### Vendas
| Método | Rota | Descrição |
|---|---|---|
| POST | `/vendas` | Criar nova venda |
| POST | `/vendas/{id}/finalizar` | Finalizar venda (baixa FEFO) |
| POST | `/vendas/{id}/cancelar` | Cancelar venda |
| GET | `/vendas` | Listar vendas |

### WebSocket
| Rota | Descrição |
|---|---|
| `ws://localhost:8000/ws/{channel}?token={jwt}` | Conectar ao canal em tempo real |

**Canais disponíveis:** `dashboard`, `estoque`, `alertas`, `vendas`, `compras`, `geral`

> Documentação completa e interativa disponível em `/docs` após rodar a API.

---

## ⚙️ Variáveis de Ambiente

Copie `.env.example` para `.env` e ajuste:

```bash
cp .env.example .env
```

| Variável | Padrão | Descrição |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./pharmacy_erp.db` | URL de conexão com o banco |
| `JWT_SECRET_KEY` | gerado automaticamente (dev) | **Obrigatório em produção** |
| `JWT_ALGORITHM` | `HS256` | Algoritmo JWT |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Expiração do token |
| `DEBUG` | `True` | Modo debug |

> ⚠️ Em produção, defina `JWT_SECRET_KEY` com uma string aleatória forte. A aplicação não sobe sem ela quando `ENV=production`.

---

## 🧪 Testes

```bash
# Rodar todos os testes
pytest tests/ -v

# Resultado esperado
# 10 passed, 15 warnings in ~3.5s
```

**Cobertura dos testes:**
- ✅ 6 testes de autenticação (registro, login, rotas protegidas)
- ✅ 2 testes de medicamentos (CRUD)
- ✅ 2 testes de vendas (criar e cancelar)

---

## 🏗️ Arquitetura

O projeto segue uma arquitetura em camadas inspirada em **Domain-Driven Design**:

```
Requisição HTTP
      ↓
  API Routes        ← Validação (Pydantic), autenticação (JWT)
      ↓
  Services          ← Lógica de negócio (FEFO, alertas, cálculos)
      ↓
  Domain Models     ← Entidades ORM (SQLAlchemy 2.0)
      ↓
  Infrastructure    ← Banco de dados (SQLite / PostgreSQL)
```

### FEFO — First Expired, First Out

Conformidade farmacêutica automática: ao finalizar uma venda, o sistema seleciona o lote com a data de validade mais próxima. O `lote_id` é armazenado em cada item de venda para rastreabilidade completa.

### WebSocket em Tempo Real

Após finalizar uma venda, o `VendaService` faz broadcast para os canais `vendas` e `estoque`. Qualquer dashboard conectado atualiza os dados sem necessidade de refresh.

---

## 📄 Licença

Distribuído sob a licença MIT. Veja [LICENSE](./LICENSE) para mais detalhes.
