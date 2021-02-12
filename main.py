from requests import get
from twilio.rest import Client
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "_YOUR_SID_HERE"
auth_token = '_YOUR_KEY_HERE_'
weather_params = {
    "lat": "22.6288",
    "lon": "88.4311",
    "exclude": "current,daily,minutely",
    "appid": "_YOUR_API_KEY_HERE",
    "hourly":"hourly.weather"
}

OWM_response = get(OWM_endpoint, params=weather_params)
OWM_response.raise_for_status()
weather_data = OWM_response.json()
first_12_hours = weather_data['hourly'][:12]
id = []
for j in range(0, 12):
    for k in first_12_hours[j]['weather']:
        id.append(int(k['id']))
for i in id:
    if i < 700:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's probably gonna rain, so bring an ☔",
            from_='whatsapp:_YOUR_TWILIO_PHONE_HERE_',
            to='whatsapp:_YOUR_PHONE_HERE_'
        )
        print(message.status)
        break
