import urllib.request
from bs4 import BeautifulSoup
import sys

CURRENCY_SITE = 'http://www.cbr.ru/scripts/XML_daily.asp'
currrency = {}


def currency_rates(code_currency):
    req = urllib.request.urlopen(CURRENCY_SITE).read()
    soup = BeautifulSoup(req, 'xml')
    valutes = soup.find_all('Valute')
    data = soup.find('ValCurs').get('Date').replace('.', '-')
    for item in valutes:
        currrency[item.find('CharCode').text] = float(item.find('Value').text.replace(',', '.'))
    print(currrency.get(code_currency.upper()), data)


if __name__ == '__main__':
    text = input('Введите валюту: '.upper())
    currency_rates(text)
    if len(sys.argv) > 1:
        external_call = sys.argv[1].upper()
        currency_rates(external_call)
