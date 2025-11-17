from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/orders')
def orders():
    return jsonify([
        {"id": 101, "user_id": 1, "item": "Notebook"},
        {"id": 102, "user_id": 2, "item": "Mouse"},
        {"id": 103, "user_id": 3, "item": "Teclado"}
    ])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)