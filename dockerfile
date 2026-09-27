# Utiliser une image officielle Python légère
FROM python:3.10-slim

# Définir le dossier de travail dans le conteneur
WORKDIR /app

# Copier le fichier des dépendances et les installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code source et le dossier des modèles
COPY . /app

# Exposer le port sur lequel l'API va écouter
EXPOSE 8000

# Commande pour lancer l'API avec Uvicorn
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]