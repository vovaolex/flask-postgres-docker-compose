from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM tasks ORDER BY id")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify([
        {"id": row[0], "title": row[1]}
        for row in rows
    ])


@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    title = data.get("title")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s) RETURNING id",
        (title,)
    )

    task_id = cursor.fetchone()[0]
    conn.commit()

    cursor.close()
    conn.close()

    return {
        "id": task_id,
        "title": title
    }, 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)