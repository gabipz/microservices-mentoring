# 1. Escolher uma imagem base
FROM python:3.13.1-slim

RUN pip install poetry

# Configurar o diretório de trabalho dentro do container
WORKDIR /app

# Copiar arquivos do seu projeto para dentro do container
COPY pyproject.toml poetry.lock ./
COPY . .

# Instalar as dependências do projeto
RUN poetry install --no-dev

# Expor a porta que o Flask usará (geralmente 5000)
EXPOSE 5000

# 7. Definir o comando padrão para rodar a aplicação
CMD ["poetry", "app.py"]
