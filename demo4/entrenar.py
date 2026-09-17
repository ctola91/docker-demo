"""
Script de entrenamiento: genera el archivo model.pkl que consume app.py
 
Ejemplo con el dataset Iris (clasificación de flores) solo para
demostrar el flujo completo. Reemplaza la carga de datos y el modelo
por los de tu propio proyecto.
"""
 
import joblib
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
 
# 1. Cargar datos
datos = load_iris()
X, y = datos.data, datos.target
 
# 2. Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
 
# 3. Entrenar el modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)
 
# 4. Evaluar
predicciones = modelo.predict(X_test)
precision = accuracy_score(y_test, predicciones)
print(f"Precisión en datos de prueba: {precision:.2%}")
 
# 5. Guardar el modelo entrenado
joblib.dump(modelo, "model.pkl")
print("Modelo guardado como model.pkl")
 