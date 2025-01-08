# Mentoria - microsserviços com Flask e Docker

## Plano de estudos
- [x] Arquitetura de microsserviços (Flask)
- [ ] Docker
- [ ] Desafio
- [ ] Apresentação

## Objetivo 
- Compreender as vantagens de uma arquitetura de microsserviços.
- Conceitos de microsserviços e Docker.
- Como utilizar o Docker para construção de um microsserviço Python.


## 1. Microsserviços usando flask

Vídeos rápido para contextualizar:
- [Youtube: Código fonte - microsserviços](https://www.youtube.com/watch?v=_2bDOCTnbKc)

Leitura:
- [Desenvolvimento de Microserviços Python: 13 Melhores Práticas](https://www.planeks.net/microservices-development-best-practices/). Seleção das sessões para ler:
	- Por que Python é ideal para Arquitetura de microsserviços
	- Comunicação de serviço
	- Conteinerização com Docker
	- Fazer **Case Study**

Conceitos envolvidos no caso de uso:
- Desenvolver app em flask
- Microsserviços
- Ambiente virtual (venv)


## 2. Docker

**Objetivo**: **Objetivo**: rodar a aplicação usando Docker.

#### Pré-requisito: Docker instalado

Para instalar o Docker, seguir o tutorial da própria documentação: https://docs.docker.com/engine/install/

Verificar funcionamento:
```shell
docker --version
```

### 2.1 - Adicionar arquivo `Dockerfile`

Para encontrar imagem (no caso, Python): [Docker Hub](https://hub.docker.com/_/python/tags?page=2).

A estrutura do Dockerfile está localizada [neste arquivo](Dockerfile).


### 2.2 - Adicionar host e porta no `app.py`

```python
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 2.3 - Construir a imagem Docker

No terminal, vá para o diretório onde está seu projeto (que contém o `Dockerfile`) e rode o seguinte comando:
```shell
docker build -t flask-microservice .
```

### 2.4 - Rodar container
```shell
docker run -d -p 5000:5000 flask-microservice
```

### 2.5 - Testar aplicação

http://localhost:5000

