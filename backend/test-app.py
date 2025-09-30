from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS para permitir peticiones desde React

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message="FUNCIONA: Este mensaje viene de Flask")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
