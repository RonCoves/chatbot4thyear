# Flask_Server.py
from flask import Flask, request, jsonify
import sys

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        print("Request received!")
        data = request.json
        user_input = data.get("message", {}).get("text", "")
        print(f"User Input: {user_input}")
        response_text = f"Echo: {user_input}"
        print(f"Response Text: {response_text}")
        return jsonify({"text": response_text})
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0', port=8081)
    except Exception as e:
        print(f"Failed to run the app. Error: {e}", file=sys.stderr)
