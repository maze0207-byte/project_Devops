from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route("/addrec", methods=['POST'])
def addrec():
    data = request.form.to_dict()     # تحويل البيانات لقاموس
    print("Received Form Data:", data)

    # قراءة URL الخاص بالـ backend
    backend_url = os.getenv("BACKEND_URL", "http://backend:5000")

    try:
        # أرسل POST للـ backend
        response = requests.post(f"{backend_url}/test", json=data, timeout=3)
        print("Backend Response:", response.text)
    except Exception as e:
        print("Error connecting to backend:", e)
        return jsonify({"error": "backend not reachable"}), 500

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001, host="0.0.0.0")
