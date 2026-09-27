from fastapi import FastAPI
import joblib
import numpy as np
import os

app = FastAPI(title="Wi-Fi MLOps API", version="1.0")

# Charger le modèle entraîné au démarrage de l'API
MODEL_PATH = "models/model.joblib"

if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    model = None

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur l'API MLOps de prédiction de congestion Wi-Fi !"}

@app.post("/predict")
def predict_congestion(rssi: float, throughput: float, clients_count: int):
    if model is None:
        return {"error": "Modèle introuvable. Veuillez exécuter l'entraînement d'abord."}
    
    # Préparer les données pour la prédiction
    features = np.array([[rssi, throughput, clients_count]])
    prediction = model.predict(features)
    probability = model.predict_proba(features)

    is_congested = bool(prediction[0])
    confidence = float(np.max(probability))

    return {
        "congestion_detected": is_congested,
        "confidence": round(confidence, 2),
        "input_features": {
            "rssi": rssi,
            "throughput": throughput,
            "clients_count": clients_count
        }
    }