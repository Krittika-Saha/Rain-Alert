from requests import get
from twilio.rest import Client
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "Your_sid_here"
auth_token = 'Your_auth_token_here'
weather_params = {
    "lat": "22.6288",
    "lon": "88.4311",
    "exclude": "current,daily,minutely",
    "appid": "_Your_api_key_here",
    "hourly":"hourly.weather"
}

OWM_response = get(OWM_endpoint, params=weather_params)
OWM_response.raise_for_status()
weather_data = OWM_response.json()
first_12_hours = [i for i in weather_data['hourly'] if weather_data['hourly'].index(i) <= 11]
id = []
for j in range(0, 12):
    for k in first_12_hours[j]['weather']:
        id.append(int(k['id']))
for i in id:
    if i < 900:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's probably gonna rain, so bring an ☔",
            from_='whatsapp:_Your_Number_Here_',
            to='whatsapp:_Your_Number_Here_'
        )
        print(message.status)
        break
