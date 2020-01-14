import requests # GET function
from bs4 import BeautifulSoup # Reading HTML

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'lxml') # Parsing the response
print(soup)

quotes = soup.find_all('span', class_='text') # Use Inspect in webpage
author = soup.find_all('small', class_='author')
tags2 = soup.find_all('div', class_='tags')

for i in range (0,len(quotes)):
    print(quotes[i].text)
    print(author[i].text)
    tags = tags2[i].find_all('a', class_='tag') # Since there are multiple tags for one quote
    for tag in tags:
        print((tag.text))