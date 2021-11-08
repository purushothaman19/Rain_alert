import requests
import os
from twilio.rest import Client

API = '5a7af1cdebc3053b2ede14ca80d7df02'
LATE = -6.175110
LONG = 106.865036

location = {
    'lat': LATE,
    'lon': LONG,
    'appid': API,
    'exclude': 'current,minutely,daily'
}

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5c10d847bfdbaa2bb866e38b4f7d76a4'
auth_token = 'eed26cf09c9e448ac42b82ce83c51af9'
client = Client(account_sid, auth_token)

connection = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=location)
# print(connection.status_code)
data = connection.json()
# print(data['hourly'][0]['weather'][0]['id'])
weather_data = data['hourly'][:12]
will_rain = False

for hour in weather_data:
    condition_code = hour['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('BRING UMBRELLA')
    message = client.messages \
        .create(
            body="Hey, Its gonna rain today. Bring an umbrella with you ☔️",
            from_='+16028832109',
            to='+919976576720'
        )

    print(message.status)
