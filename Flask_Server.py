# Flask_server
# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        user_input = data.get("message", {}).get("text", "")
        response_text = f"Echo: {user_input}"
        return jsonify({"text": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
