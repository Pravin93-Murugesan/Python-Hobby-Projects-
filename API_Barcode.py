# Converting Barcode to product information with API Calls
 
import requests
import json # JSON is not a native data structure in Python

baseURL = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '717753076632'} # Ditionary with key & value
response = requests.get(baseURL, params=parameters)
#print(response.url)

content = response.content
info = json.loads(content) # Converts to a dictionary
#print(type(info))
#print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
print(brand)
print(title)

