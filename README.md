# API de Usuários (Flask)

API simples em Flask para gerenciar usuários em memória.

## Visão geral
- Projeto minimalista: rotas, serviço e modelo.
- Armazenamento em memória (sem persistência).
- Não exponha em produção.

## Requisitos
- Python 3.8+
- Flask

## Instalação
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install Flask

python [app.py](http://_vscodecontentref_/0)
# A API roda em http://127.0.0.1:5000

Endpoints
GET /users
Retorna lista de usuários (JSON).

GET /users/<cpf>
Retorna usuário por CPF — 200 se encontrado, 404 caso contrário.

POST /users
Cria usuário. Corpo JSON esperado:
{ "name": "...", "email": "...", "password": "...", "cpf": "..." }
Respostas: 201 (criado) ou 400 (erro).

DELETE /users/<cpf>
Remove usuário por CPF — 200 sucesso, 404 não encontrado.

Observações de segurança
Método User.to_dict() não deve expor a senha por padrão.
Dados não persistem entre reinícios.
Testes
Se houver testes:
python -m pytestpython -m pytest

Estrutura importante
app.py
controllers/user_controller.py
services/user_service.py
models/user_model.py
Contribuição
Abra issues ou PRs com melhorias.

Licença
Sem licença especificada (adicione um LICENSE se desejar).