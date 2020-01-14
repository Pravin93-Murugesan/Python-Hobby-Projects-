# Open Weather
 
import requests

baseURL = 'https://api.openweathermap.org/data/2.5/forecast'
# Ditionary key APPID is specific to this website
parameters = {'APPID':'87c5e7f6eb8d0f0989667f8c9ea58785', 'q':'Aalborg, DK'} 
response = requests.get(baseURL, params=parameters)
print(response.content)