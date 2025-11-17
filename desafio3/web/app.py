from flask import Flask
import redis
import psycopg2
import os


app = Flask(__name__)


# Redis
cache_host = os.getenv("CACHE_HOST", "cache")
redis_client = redis.Redis(host=cache_host, port=6379)


# PostgreSQL
db_host = os.getenv("DB_HOST", "db")
conn = psycopg2.connect(
    dbname="desafio3",
    user="admin",
    password="admin123",
    host=db_host
)


@app.route("/")
def index():
    # Teste Redis
    redis_client.set("visitas", int(redis_client.get("visitas") or 0) + 1)
    visitas = redis_client.get("visitas").decode()


    # Teste banco
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    agora = cur.fetchone()[0]
    cur.close()


    return {
        "status": "ok",
        "visitas_cache": visitas,
        "hora_db": str(agora)
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)