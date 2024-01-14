# chatbot.py
import requests

def send_message(message):
    url = "https://flaskproj4thyr.azurewebsites.net/webhook"  # Updated URL
    payload = {"message": {"text": message}}
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(url, json=payload, headers=headers)

        print(f"Request Sent: {response.request.url}")
        print(f"Request Body: {response.request.body}")
        print(f"Response Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")

        if response.status_code == 200 and response.text:
            return response.json()["text"]
        else:
            print(f"Error: {response.status_code}")

        return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    while True:
        user_input = input("You:  ")
        response = send_message(user_input)

        if response is not None:
            print(f"Bot: {response}")