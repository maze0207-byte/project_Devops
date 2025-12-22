from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
CORS(app)

# -----------------------------
# Database Config
# -----------------------------
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

# -----------------------------
# ROUTES
# -----------------------------
@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['POST'])
def addrec():
    data = request.get_json()
    print("Received Form Data:", data)

    user_id = data.get('id')
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not all([user_id, name, email, password]):
        return jsonify({"message": "Missing data"}), 400

    hashed_password = generate_password_hash(password)

    cur = mysql.connection.cursor()
    try:
        query = "INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)"
        cur.execute(query, (user_id, name, email, hashed_password))
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({"message": "User already exists"}), 409
    finally:
        cur.close()

    return jsonify({"message": "User registered successfully", "data": data}), 201

# -----------------------------
# LOGIN API
# -----------------------------
@app.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"message": "Missing credentials"}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT password FROM users WHERE email = %s", (email,))
    user = cur.fetchone()
    cur.close()

    if user and check_password_hash(user[0], password):
        return jsonify({"message": "Login successful"}), 200

    return jsonify({"message": "Invalid email or password"}), 401

# -----------------------------
# TEST API
# -----------------------------
@app.route("/test", methods=['GET'])
def test():
    return jsonify({"status": "API is working"}), 200

# -----------------------------
# RUN FLASK
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
