# Utilisez l'image Python officielle
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requis dans le conteneur
COPY bcancer.py /app
COPY test.py /app
COPY requirements.txt /app

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Commande d'exécution par défaut
CMD ["python", "bcancer.py"]
