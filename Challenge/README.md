# Desafio

## Objetivo
Desenvolver um **microsserviço** para gerenciar propostas de crédito. 

O serviço deve receber que a empresa receba (POST) e liste (GET) as propostas de crédito enviadas pelos clientes. Utilize como microsserviço o **FastAPI** e empacotado com **Docker**.

## Requisitos

### 1. Funcionalidades do microsserviço

- **Cadastrar uma nova proposta de crédito**:
    - Endpoint: `POST /api/proposals`
    - Deve incluir:
        - ID único.
        - Nome do cliente.
        - Valor solicitado.
    - Validação de valor (lógica):
	    - Se o valor solicitado for menor que zero:
		    - **Status**: `Amount cannot be negative` (erro).
		    - **Ação**: Rejeite a proposta imediatamente, retornando um erro HTTP `400`.
		- Se o valor solicitado for menor ou igual a 10.000:
			- **Status**: `Approved`.
		- Se o valor solicitado for maior que 50.000:
			- **Status**: `Rejected`.
		- Se o valor solicitado estiver entre 10.001 e 50.000 (inclusive):
			- **Status**: `Pending`.
	      
- **Listar todas as propostas de crédito**:
    - Endpoint: `GET /api/proposals`
    - Retorna todas as propostas cadastradas.

- **Consultar uma proposta específica pelo ID**:
    - Endpoint: `GET /api/proposals/{proposal_id}`
    - Retorna a proposta correspondente ou um erro 404 se não encontrada.

#### Exemplo de cadastro
```json
{
  "id": 1,
  "customer_name": "Bruna",
  "amount": 10000
}
```

O retorno deve ser o status:

```json
{
  "status": "Approved"
}
```

### 2. Empacotamento com Docker

- O microsserviço deve ser executável dentro de um contêiner Docker.
- Crie um arquivo `Dockerfile` para empacotar o serviço.


# Material de apoio

- Youtube: Curso de FastAPI - Criando Rotas CRUD | Aula 03

    Não há necessidade de assistir o vídeo inteiro, com **APENAS** estes tópicos é possível ter uma base legal:
    - [Estrutura dos dados (User)](https://www.youtube.com/watch?v=WnhDgVLYfx0&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP&index=5)
    - [A rota (post /users/)](https://www.youtube.com/watch?v=WnhDgVLYfx0&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP&index=5&t=1004s)
    - [A rota (get /users/)](https://www.youtube.com/watch?v=WnhDgVLYfx0&list=PLOQgLBuj2-3IuFbt-wJw2p2NiV9WTRzIP&index=5&t=3798s)
