# Fiap Car Resale
Projeto desenvolvido para a pós-graduação em Arquiteura de Software da FIAP.

## Objetivo
O objetivo deste projeto é criar um sistema de revenda de carros, onde o usuário poderá cadastrar carros para venda e também comprar carros.

## Funcionalidades
- Cadastro de carros
- Compra de carros
- Listagem de carros
- Exclusão de carros

## Tecnologias
- Python
- FastAPI
- PostgreSQL
- Alembic

## Como executar
Para executar o projeto, siga os passos abaixo:
1. Clone este repositório:
```bash
git clone https://github.com/alissonit/fiap-car-resale.git
```
2. Acesse a pasta do projeto:
```bash
cd fiap-car-resale
```

3 importante crie um ambiente virtual para instalar as dependências
```bash
python -m venv .venv
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute o projeto:
```bash
uvicorn app.main:app --reload
```

## Tipo de Arquitetura
A arquitetura utilizada foi a hexagonal, onde o core da aplicação é independente de frameworks e bibliotecas externas.

## Documentação
A documentação da API pode ser acessada em:
http://localhost:8000/api/v1/docs


### Entregas
- [x] Login
- [x] Cadastro de usuário
- [x] Cadastrar um veículo para venda (Marca, modelo, ano, cor, preço)
- [x] Editar os dados do veículo
- [ ] Disponibilizar um endpoint (webhook) para que a entidade que processa o pagamento
consiga, a partir do código do pagamento, informar se o pagamento foi efetuado ou
cancelado;
