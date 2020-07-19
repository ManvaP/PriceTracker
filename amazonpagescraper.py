import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Acer-SB220Q-Ultra-Thin-Frame-Monitor/dp/B07CVL2D2S/ref=sr_1_3?dchild=1&keywords=monitor&qid=1595191992&sr=8-3'
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

page = requests.get(url, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

title = soup.find(id="productTitle").get_text()
#soup.select('#productTitle')
price = soup.find(id="priceblock_ourprice").get_text()

print(title.strip())
print(price.strip())