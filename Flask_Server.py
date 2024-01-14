# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        user_input = data.get("message", {}).get("text", "")

        # Your logic to generate a response based on user_input
        # In this example, I'm echoing the user's input
        response_text = f"Echo: {user_input}"

        # Return the response
        return jsonify({"text": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)