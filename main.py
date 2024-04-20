from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client


load_dotenv()


def send_sms():
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body='Today is rainy. Get an umbrella',
        from_=from_number,
        to='+995591103783'
    )

    print(message.sid)

api_key = os.environ.get("API_KEY")

base_url = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "q": "Istanbul,Turkey",
    "cnt": 4,
    "appid": api_key
}

response = requests.get(base_url, params=params)
weather_data = response.json()

is_rain_today = False

# for i in range(0, 4):
#     if weather_data["list"][i]["weather"][0]["main"] == "Rain":
#         is_rain_today = True
#         break

for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["main"] == "Rain":
        is_rain_today = True
        break

if is_rain_today:
    send_sms()




