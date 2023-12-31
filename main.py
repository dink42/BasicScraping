import requests
from bs4 import BeautifulSoup

headers = {
    'Acess-Control-Allow-Origin': '*',
    'Acess-Control-Allow-Methods': 'GET',
    'Acess-Control-Allow-Headers': 'Content-Type',
    'Acess-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (x11; Ubuntu; Linux x86_x64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

url = "http://example.com"
req = requests.get(url, headers)
soup = BeautifulSoup(req.content, 'html.parser')


print(soup.prettify())
