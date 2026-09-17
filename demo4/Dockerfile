FROM python:3.12-slim
 
WORKDIR /app
 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copia el código de la API y el modelo entrenado
COPY api.py .
COPY model.pkl .
 
EXPOSE 8000
 
# Usuario no root por seguridad
RUN useradd -m apiuser
USER apiuser
 
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]