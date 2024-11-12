import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

quotes = []
for quote in soup.find_all('div', class_='quote'):
    text = quote.find('span', class_='text').get_text()
    author = quote.find('small', class_='author').get_text()
    tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]

    quotes.append({
        'quote': text,
        'author': author,
        'tags': tags
    })

with open('quotes.json', 'w') as json_file:
    json.dump(quotes, json_file)