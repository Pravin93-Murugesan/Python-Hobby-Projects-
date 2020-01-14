# Open Weather
# Create a free account to make API requests
 
import requests

baseURL = 'https://api.openweathermap.org/data/2.5/forecast'
# Ditionary key APPID is specific to this website
parameters = {'APPID':'enter your key', 'q':'Aalborg, DK'} 
response = requests.get(baseURL, params=parameters)
print(response.content)
