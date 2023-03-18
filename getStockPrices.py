import requests
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate
def stockData(symbol):
    #get url
    url = f"https://uk.finance.yahoo.com/quote/{symbol}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    # get stock prices
    stock = {
        'symbol' : symbol,
        'price' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[0].text,

        'change' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[1].text,

        'unit' : soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('fin-streamer')[2].text,
    }
    stock_prices = pd.DataFrame(stock.items(),columns=['keys','values'])
    stocks = tabulate(stock_prices,headers='keys',tablefmt='psql')

    #get summary table
    name = soup.find('table', {'class': 'W(100%)'}).find_all(
        'td', {'class': 'C($primaryColor) W(51%)'})
    names = []
    for n in name:
        names.append(n.text)

    value = soup.find('table', {'class': 'W(100%)'}).find_all(
        'td', {'class': 'Ta(end) Fw(600) Lh(14px)'})
    values =[]
    for v in value:
        values.append(v.text)
    df = pd.DataFrame({'name': names,
                       'value': values
                       },columns=['name','value'])
    table = tabulate(df, headers='keys', tablefmt= 'psql')

    return stocks,table

stocks, table = stockData('ASPL.L')
print(stocks, table)
