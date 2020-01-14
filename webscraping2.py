#From multiple webpages

import requests
from bs4 import BeautifulSoup 

url = 'https://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
count = 1
for item in items:  
    name = item.find('h4', class_='card-title').text.strip('\n') #Remove new line
    price = item.find('h5').text
    print('%s) Name: %s, Price: %s' % (count, name, price))
    count = count + 1

pages = soup.find('ul', class_='pagination')
pagelinks = pages.find_all('a', class_='page-link')
urls = []

for link in pagelinks:
    #pagenum = int(link.text) if link.text.isdigit() else None  
    #if pagenum != None:
    if link.text.isdigit():
        x = link.get('href')
        urls.append(x)
    else:
        None
print(urls)

count = 1
for i in urls:
    newurl = url + i
    response = requests.get(newurl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for item in items:  
        name = item.find('h4', class_='card-title').text.strip('\n') #Remove new line
        price = item.find('h5').text
        print('%s) Name: %s, Price: %s' % (count, name, price))
        count = count + 1