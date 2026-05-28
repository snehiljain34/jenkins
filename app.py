from flask import Flask, render_template, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Fetch database connection parameters dynamically from container environment variables
def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', 'secret'),
        database=os.environ.get('DB_NAME', 'app_db')
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>Two-Tier App Operational! Connected to Database Version: {db_version[0]}</h1>"
    except Exception as e:
        return f"<h1>Connection Failure! Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)