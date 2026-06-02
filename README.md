<div align="center">

<img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-0.104-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/SQLAlchemy-2.0-red?style=for-the-badge"/>
<img src="https://img.shields.io/badge/WebSocket-realtime-6DB33F?style=for-the-badge"/>

<br/><br/>

# 💊 PharmacyERP

**Sistema de Gestão Farmacêutica** — controle completo de estoque, vendas, fornecedores e relatórios com dashboard em tempo real.

Projeto acadêmico desenvolvido na disciplina de **Análise e Desenvolvimento de Sistemas** — Centro Universitário UniFavip Wyden.

</div>

---

## 📸 Interface

> Dashboard principal com KPIs, gráficos e alertas em tempo real.

<!--
  💡 DICA: tire um screenshot real do sistema rodando e salve em docs/screenshot.png
  Depois substitua o bloco SVG abaixo pela linha:
  ![Dashboard PharmacyERP](docs/screenshot.png)
-->

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────┐
│  P PharmacyERP  │  Dashboard   Estoque   Preços   Vendas   Relatórios  │
│─────────────────┼──────────────────────────────────────────────────────│
│  📊 Dashboard   │  Vendas Hoje    Medicamentos    Alertas    Vencendo  │
│  📦 Estoque     │  R$ 3.240 ↑    248 ativos       7 crítico  12 items  │
│  💰 Preços      │─────────────────────────────────────────────────────│
│  🛒 Vendas      │  Receita 7 Dias          Top Medicamentos            │
│  👥 Clientes    │  ╭──────────────╮        Dipirona 500mg ████████ 142 │
│  🚚 Fornecedores│  │  ~           │        Amoxicilina    ██████   98  │
│  📈 Relatórios  │  │    ~  ╭──╮  │        Omeprazol      █████    76  │
│                 │  ╰──────────╯──╯        Losartana      ████     54  │
│  💡 Dica do Dia │  Seg Ter Qua Sex Dom   ─────────────────────────── │
│  Revise validades│                        ⚠️ Insulina — estoque crítico│
└─────────────────┴──────────────────────────────────────────────────────┘
```

</div>

---

## ✨ Funcionalidades

| Módulo | Descrição |
|---|---|
| 🏠 **Dashboard** | KPIs em tempo real — vendas do dia, ticket médio, alertas críticos e gráfico de receita semanal |
| 📦 **Estoque** | Cadastro de medicamentos com código EAN, controle por lotes, alertas de validade e filtros |
| 💰 **Preços** | Gestão de preço de custo e venda com cálculo automático de margem |
| 🛒 **Vendas** | PDV com busca por nome, carrinho, formas de pagamento e emissão de recibo |
| 👥 **Clientes** | Cadastro e histórico de compras por cliente |
| 🚚 **Fornecedores** | Cadastro completo com CRUD e vinculação a pedidos de compra |
| 📊 **Relatórios** | Gráficos de top medicamentos vendidos, receita por período e exportação CSV |
| 🔔 **Alertas** | Notificações automáticas de estoque baixo e medicamentos próximos ao vencimento |
| ⚡ **WebSocket** | Atualizações em tempo real no dashboard sem necessidade de recarregar a página |

---

## 🏗️ Arquitetura

O projeto segue os princípios do **Domain-Driven Design (DDD)**, separando responsabilidades em camadas bem definidas:

```
PharmacyERP/
│
├── Domain/                  # Entidades e regras de negócio
│   ├── Medicamento.py
│   ├── Venda.py
│   ├── Lote.py
│   ├── Fornecedor.py
│   ├── Compra.py
│   ├── Alerta.py
│   └── Enums/               # StatusCompra, StatusLote, TipoAlerta
│
├── Application/             # Casos de uso e serviços de aplicação
│   └── services/
│       ├── medicamento_service.py
│       ├── venda_service.py
│       ├── relatorio_service.py
│       ├── alerta_service.py
│       └── ...
│
├── Infrastructure/          # Banco de dados e configurações
│   ├── database.py          # SQLAlchemy + SQLite
│   ├── seeds.py             # Dados de demonstração
│   └── logger.py
│
├── API/                     # Camada de apresentação
│   ├── main.py              # Aplicação FastAPI
│   ├── routes/              # Endpoints REST por domínio
│   │   ├── medicamentos.py
│   │   ├── vendas.py
│   │   ├── fornecedores.py
│   │   ├── relatorios.py
│   │   ├── alertas.py
│   │   └── auth_routes.py
│   ├── websocket/           # Comunicação em tempo real
│   │   ├── manager.py
│   │   └── events.py
│   ├── schemas.py           # Schemas Pydantic (request/response)
│   ├── middleware.py        # Autenticação JWT
│   │
│   ├── index.html           # Frontend — SPA em HTML/CSS/JS puro
│   ├── Style.css
│   └── script.js
│
├── tests/                   # Testes com pytest + httpx
│   ├── test_auth.py
│   ├── test_medicamentos.py
│   └── test_vendas.py
│
├── migrations/              # Alembic — controle de versão do banco
├── docker-compose.yml
└── Requirements.txt
```

---

## 🛠️ Tecnologias

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — framework web assíncrono de alta performance
- [SQLAlchemy 2.0](https://www.sqlalchemy.org/) — ORM com Mapped types e type hints
- [Alembic](https://alembic.sqlalchemy.org/) — migrações de banco de dados
- [Pydantic v2](https://docs.pydantic.dev/) — validação e serialização de dados
- [python-jose](https://python-jose.readthedocs.io/) — autenticação JWT
- [WebSockets](https://websockets.readthedocs.io/) — comunicação bidirecional em tempo real

**Frontend**

<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
<img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white"/>
<img src="https://img.shields.io/badge/Font_Awesome-538DD7?style=for-the-badge&logo=fontawesome&logoColor=white"/>

- [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) / [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS) / [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) puro — SPA sem dependência de frameworks
- [Chart.js](https://www.chartjs.org/) — gráficos interativos e responsivos
- [Font Awesome 6](https://fontawesome.com/) — biblioteca de ícones

**Banco de Dados**
- SQLite — zero configuração, portátil, pronto para rodar localmente

**Testes**
- pytest, pytest-asyncio, httpx

---

## 🚀 Como rodar

### Pré-requisitos

- Python 3.11+
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/Viniciusmbbr/PharmacyERP.git
cd PharmacyERP
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r Requirements.txt
```

### 4. Configure o ambiente

```bash
cp .env.example .env
# O projeto funciona com as configurações padrão — nenhuma edição necessária
```

### 5. Inicialize o banco de dados com dados de demonstração

```bash
python setup_database.py
```

### 6. Inicie a API

```bash
uvicorn API.main:app --reload
```

### 7. Abra o frontend

Abra o arquivo `API/index.html` diretamente no navegador.  
Recomendado: extensão **Live Server** no VS Code para recarregamento automático.

> 🔗 API disponível em `http://localhost:8000`  
> 📖 Documentação interativa (Swagger UI): `http://localhost:8000/docs`

### Credenciais de demo

| Usuário | Senha | Perfil |
|---|---|---|
| admin@farmacia.com | 123456 | Administrador |
| farmaceutico@farmacia.com | 123456 | Farmacêutico |
| caixa@farmacia.com | 123456 | Operador de Caixa |

---

## 🐳 Rodando com Docker

```bash
docker-compose up --build
```

---

## 🧪 Testes

```bash
pytest tests/ -v
```

---

## 📡 Endpoints principais

| Método | Rota | Descrição |
|---|---|---|
| `POST` | `/auth/login` | Autenticação e geração de token JWT |
| `GET` | `/medicamentos` | Listar medicamentos com paginação |
| `POST` | `/medicamentos` | Cadastrar novo medicamento |
| `GET` | `/medicamentos/estoque/baixo` | Medicamentos com estoque crítico |
| `GET` | `/medicamentos/vencimento/proximo` | Medicamentos próximos ao vencimento |
| `GET` | `/vendas` | Listar vendas com paginação |
| `POST` | `/vendas` | Registrar nova venda |
| `PATCH` | `/vendas/{id}/finalizar` | Finalizar venda e baixar estoque automaticamente |
| `GET` | `/vendas/{id}/recibo` | Gerar recibo de uma venda |
| `GET` | `/fornecedores` | Listar fornecedores |
| `GET` | `/relatorios/dashboard` | KPIs e dados do dashboard |
| `GET` | `/relatorios/exportar/csv` | Exportar relatório de vendas em CSV |
| `GET` | `/alertas` | Alertas pendentes (estoque e vencimento) |
| `WS` | `/ws/{canal}` | WebSocket para atualizações em tempo real |

Documentação completa com todos os endpoints e schemas: `http://localhost:8000/docs`

---

## 🗂️ Modelo de dados

```
medicamento ──< lote
medicamento ──< alerta
medicamento ──< item_compra
medicamento ──< item_venda (via venda)

fornecedor ──< compra
compra ──< item_compra

usuario ──< venda
venda ──< item_venda
```

---

## 👤 Autor

**ViniciusMB** — Estudante de Análise e Desenvolvimento de Sistemas

[![GitHub](https://img.shields.io/badge/GitHub-Viniciusmbbr-181717?style=flat-square&logo=github)](https://github.com/Viniciusmbbr)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/seu-perfil)

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">
<sub>Desenvolvido como projeto acadêmico — Centro Universitário UniFavip Wyden · 2025/2026</sub>
</div>
