from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/users")
def users():
    return jsonify([
        {"id": 1, "nome": "Alice", "ativo_desde": "2021-01-10"},
        {"id": 2, "nome": "Bruno", "ativo_desde": "2022-03-05"}
    ])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)