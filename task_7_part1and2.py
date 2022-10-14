import matplotlib.pyplot as plt
import requests as req
from bs4 import BeautifulSoup
from tabulate import tabulate

page = req.get('https://mainfin.ru/currency/cb-rf/usd?ysclid=l98vyakeg3915912275', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 '
'Firefox/50.0'})

soup = BeautifulSoup(page.text, 'html.parser')

currency_rate = soup.find_all('td', {'class': 'float-convert'})
time = soup.find_all('a', {'class':'link'})
date, rate = reversed([time1.text for time1 in time]), reversed([currency_rate1.text for currency_rate1 in currency_rate][2:10])
sl = dict(zip(date, rate))
print(tabulate(sl.items(), headers=['Дата', 'Курс'], tablefmt='grid'))


plt.plot(list(sl.keys()), list(sl.values()), list(sl.keys()), list(sl.values()), 'ro')
plt.show()