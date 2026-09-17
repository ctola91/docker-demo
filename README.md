docker run hello-world
docker build -t myapp:1.0
docker run -d --name myapp -p 5000:5000 myapp:1.0