from flask import Flask, request, jsonify
import requests
from flask_cors import CORS
from flask_mysqldb import MySQL

app = Flask(__name__)

# Use service name NOT IP !
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)
CORS(app)

@app.route("/test", methods=['POST'])
def test():
    data = request.get_json()
    print("JSON Received:", data)

    Id = data.get('Id')
    nm = data.get('nm')
    email = data.get('nm1')

    cur = mysql.connection.cursor()

    # Safe INSERT
    query = "INSERT INTO users (id, name, email) VALUES (%s, %s, %s)"
    cur.execute(query, (Id, nm, email))

    mysql.connection.commit()

    # Fetch all data
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    print("DB Data:", users)
    cur.close()

    return jsonify({"status": "success", "received": data, "users": users}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')