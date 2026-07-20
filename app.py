import os
from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# DB config pulled from environment variables (set in docker-compose / K8s / EC2 env)
db_config = {
    "host": os.environ.get("MYSQL_HOST", "mysql"),
    "user": os.environ.get("MYSQL_USER", "root"),
    "password": os.environ.get("MYSQL_PASSWORD", "password"),
    "database": os.environ.get("MYSQL_DATABASE", "messagedb"),
}


def get_db_connection():
    return mysql.connector.connect(**db_config)


@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, message FROM messages ORDER BY id DESC")
    messages = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template("index.html", messages=messages)


@app.route("/add", methods=["POST"])
def add_message():
    name = request.form.get("name")
    message = request.form.get("message")
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO messages (name, message) VALUES (%s, %s)", (name, message)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for("index"))


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
