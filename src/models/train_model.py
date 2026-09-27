import os
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train():
    os.makedirs("models", exist_ok=True)
    os.makedirs("data", exist_ok=True)

    data_path = "data/telemetry_data.csv"
    
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
    else:
        print("⚠️ Fichier CSV introuvable, utilisation de données de test simulées.")
        df = pd.DataFrame({
            'rssi': [-50, -80, -90, -55, -75, -45, -85],
            'throughput': [50, 5, 2, 45, 10, 60, 3],
            'clients_count': [5, 20, 25, 4, 18, 3, 22],
            'congestion_label': [0, 1, 1, 0, 1, 0, 1]
        })

    X = df[['rssi', 'throughput', 'clients_count']]
    y = df['congestion_label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Entraînement du modèle Random Forest...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Précision du modèle : {acc * 100:.2f}%")

    model_output_path = "models/model.joblib"
    joblib.dump(model, model_output_path)
    print(f"Modèle sauvegardé dans : {model_output_path}")

if __name__ == "__main__":
    train()