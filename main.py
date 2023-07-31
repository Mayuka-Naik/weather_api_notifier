import requests                     # Requests module to request open data from the weather API.
from twilio.rest import Client      # Importing twilio API module.

# Twilio account authentication constants.
ACCOUNT_SID = ''
AUTH_TOKEN = ""

# Weather API authentication constants.
API_KEY = ""
API_ENDPOINT = "http://api.weatherapi.com/v1/forecast.json?"
TWILIO_RECOVERY_CODE = "bx5JbgdBYR-lRSkwSXTJ4EhNfpNOD71CSzRKPF01"
# Weather API parameters.
params = {
    "key": API_KEY,
    "q": "Bengaluru",
    "days": 1,
    "dt": "2023-08-01"
}

# First API call to get the required forecast data.
response = requests.get(url=API_ENDPOINT, params=params)
response.raise_for_status()
data = response.json()

# The hourly forecast for the next day
hourly_forecast = data['forecast']['forecastday'][0]['hour']

# The data was extracted and opened up in online JSON viewer to get the required data.
will_rain = False
for number in range(0, 24):
    if hourly_forecast[number]['will_it_rain'] == 1:
        will_rain = True
        break

# Twilio API setup to send a message.
if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(body="Carry an Umbrella tomorrow!", from_='', to='')
    print(message.status)
