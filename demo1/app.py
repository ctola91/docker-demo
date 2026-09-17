from flask import Flask, jsonify

app = Flask(__name__)

@app.get('/')
def hello():
    return jsonify("Hola mundo desde docker!")