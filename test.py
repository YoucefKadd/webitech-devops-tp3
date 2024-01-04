import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

# Charger le modèle
with open('breast_cancer_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Charger ou préparer les données de test
test_data_url = "https://raw.githubusercontent.com/AbdallahTayeb/DevOps-Course/main/sample.csv"
test_data = pd.read_csv(test_data_url, sep=";")

# Faire des prédictions
X_test = test_data.drop('target', axis=1)
y_true = test_data['target']
y_pred = model.predict(X_test)

# Calculer la précision
accuracy = accuracy_score(y_true, y_pred)
print(f"Précision sur les nouvelles données : {accuracy * 100:.2f}%")

# Définir un seuil de classification
seuil = 0.5

# Vérifier si le seuil est atteint
if accuracy >= seuil:
    print("Le modèle a une précision satisfaisante.")
else:
    print("Le modèle n'atteint pas la précision souhaitée.")
