import requests
from flask import Flask


app = Flask(__name__)


@app.route("/")
def index():
    resp = requests.get("http://service-a:5000/users")
    users = resp.json()


    linhas = []
    for u in users:
        linhas.append(f"Usuário {u['nome']} — ativo desde {u['ativo_desde']}")


    return "<br>".join(linhas)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)