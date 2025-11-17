from flask import Flask, jsonify
from datetime import datetime


app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({
    'message': 'Hello from web-server',
    'timestamp': datetime.utcnow().isoformat() + 'Z'
    })


if __name__ == '__main__':
# roda na porta 8080
    app.run(host='0.0.0.0', port=8080)