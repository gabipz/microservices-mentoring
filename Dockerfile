# 1. Escolher uma imagem base
FROM python:3.13.1-slim

# 2. Configurar o diretório de trabalho dentro do container
WORKDIR /app

# 3. Copiar arquivos do seu projeto para dentro do container
COPY requirements.txt .

# 4. Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar o restante do código
COPY . .

# 6. Expor a porta que o Flask usará (geralmente 5000)
EXPOSE 5000

# 7. Definir o comando padrão para rodar a aplicação
CMD ["python", "app.py"]
