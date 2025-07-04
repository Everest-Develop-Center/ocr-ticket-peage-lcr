# Choix de l'image de base
FROM python:3.11-slim
LABEL authors="everest-team-dev"

# Dénifition du répertoire de travail
WORKDIR /app

#Déclaration des volumes
VOLUME storage

# Installation des packages de bases
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers du projet
COPY . .

# Port exposé
EXPOSE 8000

ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--port", "8000"]