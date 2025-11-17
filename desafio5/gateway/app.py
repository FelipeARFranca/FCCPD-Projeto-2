from flask import Flask, jsonify
import requests


app = Flask(__name__)


USER_SERVICE_URL = "http://user-service-d5:8080/users"
ORDER_SERVICE_URL = "http://order-service:7000/orders"


@app.route('/users')
def users():
    resp = requests.get(USER_SERVICE_URL)
    return jsonify(resp.json())


@app.route('/orders')
def orders():
    resp = requests.get(ORDER_SERVICE_URL)
    return jsonify(resp.json())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)