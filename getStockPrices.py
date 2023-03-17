import requests
from bs4 import BeautifulSoup

url = "https://uk.finance.yahoo.com/quote/ASPL.L"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text,'html.parser')
price = soup.find('fin-streamer',{'class':'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
print(price)