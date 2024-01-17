# chatbot.py

# Import necessary libraries
import requests
import json
import logging

# Configure logging to save information to a log file
logging.basicConfig(filename='client.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def send_message(message):
    # Set up the URL and payload for the webhook
    url = "http://127.0.0.1:8082/webhook"
    payload = {"message": {"text": message}}
    headers = {"Content-Type": "application/json"}

    try:
        # Make a POST request to the webhook endpoint
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Log information about the request and response
        logging.info(f"Request Sent: {response.request.url}")
        logging.debug(f"Request Body: {json.dumps(payload)}")
        logging.info(f"Response Status Code: {response.status_code}")
        logging.debug(f"Response Content: {response.content}")

        # Check if the response is successful and contains text
        if response.status_code == 200 and response.text:
            return response.json()["text"]
        else:
            # Log error information for unsuccessful responses
            error_message = f"Error: {response.status_code}"
            logging.error(error_message)
            return None
    except requests.exceptions.RequestException as e:
        # Log errors related to the request itself
        error_message = f"Error: {e}"
        logging.error(error_message)
        return None
    except requests.exceptions.HTTPError as e:
        # Log HTTP-related errors
        error_message = f"HTTP Error: {e}"
        logging.error(error_message)
        return None
    except json.JSONDecodeError as e:
        # Log errors related to JSON decoding
        error_message = f"Error decoding JSON: {e}"
        logging.error(error_message)
        return None

if __name__ == '__main__':
    # Run an infinite loop for user interaction
    while True:
        user_input = input("You:  ")
        response = send_message(user_input)

        # Display the bot's response if available
        if response is not None:
            print(f"Bot: {response}")
