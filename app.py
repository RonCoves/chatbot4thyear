# app.py

import os
from flask import Flask, request, jsonify, render_template
from flask_talisman import Talisman
import sys
import bleach

app = Flask(__name__)
talisman = Talisman(app, force_https=False, strict_transport_security=True)


def validate_input(data):
    """
    Validate and sanitize user input from the JSON payload.
    """
    if data is None or "message" not in data or not isinstance(data["message"], dict) or "text" not in data["message"]:
        raise ValueError("Invalid JSON format or missing 'message'/'text' field.")
    return bleach.clean(data["message"]["text"])


@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint to receive and process incoming messages.
    """
    try:
        # Get JSON data from the request
        data = request.json

        # Validate and sanitize user input
        user_input = validate_input(data)

        # TODO: Implement API connection to Zendesk here
        # Example: Make API requests to Zendesk based on user_input

        # For now, just echo the user's input
        response_text = f"Echo: {user_input}"

        # Respond to the client with the echoed text
        return jsonify({"text": response_text})

    except ValueError as e:
        # Handle validation errors
        print(f"Error: {e}", file=sys.stderr)
        return jsonify({"error": str(e)}), 400  # Bad Request

    except Exception as e:
        # Handle other errors
        print(f"Error: {e}", file=sys.stderr)
        return jsonify({"error": str(e)}), 500  # Internal Server Error


@app.route('/')
def index():
    """
    Route for serving the index.html page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    try:
        # Run the Flask app on the specified port, defaulting to 8082
        app.run(debug=False, host='0.0.0.0', port=os.environ.get('PORT', 8082))
    except Exception as e:
        # Handle any errors that occur during app startup
        print(f"Failed to run the app. Error: {e}", file=sys.stderr)
