import requests
from bs4 import BeautifulSoup
import pandas as pd

def stockData(symbol):
    url = f"https://uk.finance.yahoo.com/quote/{symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    stock = {
        'symbol' : symbol,
        'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,

        'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,

        'unit' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
    }
    return stock
print(stockData('PREM.L'))
