# Fiap Car Resale Admin
Projeto desenvolvido para a pós-graduação em Arquiteura de Software da FIAP.

## Objetivo
O objetivo deste projeto é criar um sistema de revenda de veículos, onde o usuário poderá cadastrar veículos para venda e também comprar veículos.

## Funcionalidades
- Cadastro de usuários
- Delete de usuários
- listagem de usuários
- Login e logout de usuários
- Cadastro de veículos
- Update de veículos
- Delete de veículos
- Compra de veículos
- Exclusão de veículos

## Tecnologias
- Python
- FastAPI
- PostgreSQL
- Alembic

## Como executar
Para executar o projeto, siga os passos abaixo:
1. Clone este repositório:
```bash
git clone https://github.com/alissonit/fiap-car-resale-admin.git
```
2. Acesse a pasta do projeto:
```bash
cd fiap-car-resale-admin
```

3 importante crie um ambiente virtual para instalar as dependências
```bash
python -m venv .venv
```
4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. crie um arquivo .env na raiz do projeto com as seguintes variáveis de ambiente:
```bash
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
DB_NAME=
DB_URI=
DB_MAX_POOL_SIZE=
```

6. Execute o projeto:
```bash
uvicorn main:app --port 8000 --reload
```

## Tipo de Arquitetura
A arquitetura utilizada foi a hexagonal, onde o core da aplicação é independente de frameworks e bibliotecas externas.

## Documentação
A documentação da API pode ser acessada em:
http://localhost:8000/fiap-car-resale/admin/api/v1/docs


### Entregas do projeto
- [x] Login
- [x] Cadastro de usuário
- [x] Cadastrar um veículo para venda (Marca, modelo, ano, cor, preço)
- [x] Editar os dados do veículo
- [x] Excluir um veículo
- [x] Excluir um usuário

### CI/CD
- [x] Implementar Github Actions
- [x] Cobertura de testes unitários acima de 80%
- [x] Deploy no Openshift

### Infraestrutura
- [x] Cluster Openshift Red Hat.
- [x] Objetos do kubernetes (Deployment, Service, Ingress).
- [x] Banco de dados PostgreSQL RDS AWS.

# Evidências

### Cobertura de testes em 80%
![image](/images/coverage-80.png)

link do html da cobertura de testes:

[coverage](/tests/index.html)

### CI/CD

Github Actions:

![image](/images/action.png)

link do github actions: [actions](https://github.com/alissonit/fiap-car-resale-admin/actions/runs/9263097886/job/25481037030)

### Documentação da API
![image](/images/openapi-docs.png)

### Deploy K8s (Redhat Openshift)

![image](/images/openshift.png)

Evidências dos recursos criados no Openshift:

![image](/images/resources-ocp.png)

Recursos criados no Openshift:

[Kubernetes Resources](/infrastructure/kubernetes-openshift)

### Desenho da arquitetura Hexagonal

![image](/images/arquitetura-hexagonal.png)

