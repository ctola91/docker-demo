# Demos

## Demo 1

```bash
docker build -t myapp:1.0
docker run -d --name myapp -p 5000:5000 myapp:1.0
```

## Demo 2
```bash
docker compose up -d
```
docker run hello-world

## Demo 3
```bash
docker compose up -d
```

## Demo 4
```bash
docker build -t prediction-api .
docker run -p 8000:8000 prediction-api
```