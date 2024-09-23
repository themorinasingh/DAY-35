import requests
import smtplib
from twilio.rest import Client
import os

API_KEY = os.environ.get("OPEN_WEATHER_MAP_API_KEY")

account_sid = os.environ.get("TWILIO_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

parameters = {
    "appid": API_KEY,

    "lat": 50.850346,

    "lon": 4.351721,

    "cnt":4
}

response = requests.get(url=f"https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()

weather_data = response.json()
# print(weather_data['list'][0]["weather"][0]["id"])

will_rain = False

for data in weather_data['list']:
    weather_id = data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True


if will_rain:
    print("Bring an Umbrella.")

    username = "morinasingh05@gmail.com"
    password = "mbccnsakaddumiwt"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(username,password)
        connection.sendmail(from_addr=username, to_addrs="morinasing@gmail.com", msg="Subject:Bring an Umbrella \n\n Bring an Umbrella")

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='+12084083706',
        body='Bring an Umbrella, it will rain today ☔️',
        to='+15062694986'
    )

    client = Client(account_sid, auth_token)

    message_2 = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Bring an Umbrella, it will rain today ☔',
        to='whatsapp:+15062694986'
    )
