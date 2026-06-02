# Como Rodar o PharmacyERP

Este guia cobre três formas de rodar o projeto: **local simples**, **local com frontend** e **Docker**.

---

## Pré-requisitos

- Python 3.10+
- pip
- (Opcional) Docker e Docker Compose

---

## Opção 1 — Local (recomendado para desenvolvimento)

### 1. Clonar e entrar na pasta

```bash
git clone https://github.com/seu-usuario/ERPPharmacy.git
cd ERPPharmacy
```

### 2. Criar e ativar o ambiente virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependências

```bash
pip install -r Requirements.txt
```

### 4. Configurar variáveis de ambiente

```bash
# Windows
copy .env.example .env

# Linux / macOS
cp .env.example .env
```

Abra o `.env` e ajuste conforme necessário. Para desenvolvimento, os valores padrão já funcionam.

### 5. Inicializar o banco de dados

```bash
python setup_database.py
```

Isso cria o banco SQLite com as tabelas e insere dados de exemplo (seed).

### 6. Rodar a API

```bash
uvicorn API.main:app --reload --host 0.0.0.0 --port 8000
```

A API está disponível em:

| URL | Descrição |
|---|---|
| http://localhost:8000 | Health check |
| http://localhost:8000/docs | Documentação interativa (Swagger) |
| http://localhost:8000/redoc | Documentação alternativa |

**Credenciais padrão:**
- Email: `admin@pharmacy.com`
- Senha: `Admin123!`

---

## Opção 2 — Local com Frontend

Para acessar as páginas HTML (dashboard, vendas, estoque), sirva os arquivos estáticos em paralelo com a API.

**Terminal 1 — API:**
```bash
uvicorn API.main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 — Frontend:**
```bash
python -m http.server 5500 --directory ./API
```

Acesse o frontend em: **http://localhost:5500**

> As páginas já fazem requisições para `http://localhost:8000` automaticamente.

---

## Opção 3 — Docker Compose

Sobe a API, PostgreSQL e pgAdmin com um único comando.

```bash
# Copiar variáveis de ambiente
cp .env.example .env

# Subir todos os serviços
docker-compose up
```

Para rodar em segundo plano:
```bash
docker-compose up -d
```

| Serviço | URL |
|---|---|
| API | http://localhost:8000 |
| Docs | http://localhost:8000/docs |
| pgAdmin | http://localhost:5050 |

Credenciais pgAdmin: `admin@pharmacy.com` / `admin`

Para parar:
```bash
docker-compose down
```

Para ver os logs:
```bash
docker-compose logs -f backend
```

---

## Rodando os Testes

```bash
pytest tests/ -v
```

Resultado esperado: `10 passed` em ~3.5 segundos.

---

## Solução de Problemas

**`ModuleNotFoundError`**
Verifique se o ambiente virtual está ativado e as dependências foram instaladas.

**`Connection refused` no frontend**
A API não está rodando. Verifique o Terminal 1 e confirme que aparece `Uvicorn running on http://127.0.0.1:8000`.

**`CORS Error` no navegador**
Reinicie a API. Se persistir, confirme que está acessando o frontend via `http://localhost:5500` e não pelo caminho do arquivo (`file://`).

**Porta 8000 ou 5500 já em uso**
```bash
# Trocar a porta da API
uvicorn API.main:app --reload --port 8001

# Trocar a porta do frontend
python -m http.server 5501 --directory ./API
```

**Banco de dados corrompido ou sem dados**
```bash
del pharmacy_erp.db      # Windows
rm pharmacy_erp.db       # Linux/macOS
python setup_database.py
```

---

## Variáveis de Ambiente Principais

| Variável | Padrão | Descrição |
|---|---|---|
| `DATABASE_URL` | `sqlite:///./pharmacy_erp.db` | Conexão com o banco |
| `JWT_SECRET_KEY` | gerado automaticamente | **Obrigatório definir em produção** |
| `DEBUG` | `True` | Ativa logs detalhados |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` | Validade do token JWT |

> Em produção, defina `ENV=production` e `JWT_SECRET_KEY` com um valor seguro. A aplicação **não inicializa** sem essa variável em modo produção.
