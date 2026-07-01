# Task List REST API

API RESTful para gerenciamento de tarefas, desenvolvida com **Django** e **Django REST Framework**. A estrutura inclui configurações de CORS voltadas para integração com o frontend (porta 4200, padrão do Angular).

## Tecnologias

- Python 3
- Django & Django REST Framework
- MySQL
- python-dotenv (para variáveis de ambiente)

## Funcionalidades

- CRUD completo de tarefas (GET, POST, PUT, DELETE).
- Modelagem das tarefas com: título, descrição, status de conclusão, data de criação e categoria.

## Como rodar o projeto localmente

### 1. Banco de Dados (MySQL)
Crie o schema no seu banco:
```sql
CREATE SCHEMA `tasks` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci ;
```

### 2. Configuração do Ambiente e Dependências
Crie e ative o ambiente virtual na raiz do projeto:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências. Como o repositório possui o arquivo `requirements.txt`, basta rodar:
```bash
pip install -r requirements.txt
```
*(Se houver erro com o `mysqlclient` no Ubuntu/Debian, instale: `sudo apt install python3-dev default-libmysqlclient-dev build-essential`)*

### 3. Variáveis de Ambiente
Crie um arquivo `.env` na raiz (baseado no `.env.example`) e configure os dados:
```env
DB_NAME=task-list
DB_USER=seu-usuario
DB_PASSWORD=sua-senha
DB_HOST=127.0.0.1
DB_PORT=3306

SECRET_KEY=sua_chave_secreta
DEBUG=True
```

### 4. Migrations e Execução
Aplique as alterações no banco de dados:
```bash
python manage.py makemigrations tasks
python manage.py migrate
```

Inicie o servidor:
```bash
python manage.py runserver
```

A API estará rodando em: `http://localhost:8000/api/tasks/`

## Endpoints Principais

Devido a configuração da classe ModelViewSet em ```tasks/views.py```, a rota `/api/tasks/` disponibiliza automaticamente os seguintes métodos:

- `GET`: Lista todas as tarefas.
- `POST`: Cria uma tarefa.
- `GET {id}`: Exibe uma tarefa.
- `PUT {id}`: Atualiza uma tarefa.
- `DELETE {id}`: Exclui uma tarefa.