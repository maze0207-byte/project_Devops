from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates', static_folder='static')
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
# DELETE USER API
# -----------------------------
@app.route("/delete_user", methods=['DELETE'])
def delete_user():
    data = request.get_json()
    user_id = data.get('id')
    email = data.get('email')

    if not user_id and not email:
        return jsonify({"message": "Provide id or email to delete"}), 400

    cur = mysql.connection.cursor()

    try:
        # تحقق إذا المستخدم موجود
        if user_id:
            cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        else:
            cur.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cur.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        # احذف المستخدم
        if user_id:
            cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
        else:
            cur.execute("DELETE FROM users WHERE email = %s", (email,))
        mysql.connection.commit()
    except Exception as e:
        mysql.connection.rollback()
        return jsonify({"message": "Error deleting user", "error": str(e)}), 500
    finally:
        cur.close()

    return jsonify({"message": "User deleted successfully"}), 200

@app.route("/test", methods=['GET'])
def test():
    return jsonify({"status": "API is working"}), 200

# -----------------------------
# RUN FLASK
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
