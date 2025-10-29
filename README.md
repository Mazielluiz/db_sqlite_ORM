# Python ORM

Um projeto de exemplo usando SQLAlchemy ORM para gerenciar clientes e pedidos.

## Estrutura do Projeto

- `app.py`: Arquivo principal com as operações CRUD
- `config/`: Configurações do projeto
  - `base.py`: Configuração do banco de dados
  - `settings.py`: Configurações globais
- `models/`: Modelos do banco de dados
  - `customer.py`: Modelo de Cliente
  - `order.py`: Modelo de Pedido

## Como usar

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv .venv`
3. Ative o ambiente virtual:
   - Windows: `.venv\Scripts\activate`
   - Linux/Mac: `source .venv/bin/activate`
4. Instale as dependências: `pip install sqlalchemy`
5. Execute o programa: `python app.py`

## Funcionalidades

- Criação de clientes
- Registro de pedidos
- Consulta de clientes e seus pedidos
- Relacionamento entre cliente e pedidos