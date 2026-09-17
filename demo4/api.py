import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI(title="API de Predicción")
 
# Carga el modelo entrenado (debe existir model.pkl en la misma carpeta)
modelo = joblib.load("model.pkl")
 
 
class Entrada(BaseModel):
    features: list[float]
 
 
@app.get("/")
def inicio():
    return {"mensaje": "API de predicción funcionando correctamente"}
 
 
@app.post("/predict")
def predecir(datos: Entrada):
    X = np.array(datos.features).reshape(1, -1)
    prediccion = modelo.predict(X)
    return {"prediccion": prediccion.tolist()}
 
 
@app.get("/health")
def salud():
    return {"status": "ok"}