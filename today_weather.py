import requests
responses=response("http://www.metweather.com/api/location/search/?query=banglore")

for responses in responses.json():
    woeid=str(responses['woeid'])
    weatherJSON=currrent_weather.json()
    print("The weather conditions for" + response['title'] + "today is" + weatherJSON['consolidated_weather'][0]['weather_state_name'])
