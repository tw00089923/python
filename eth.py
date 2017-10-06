#crawl ethereum rate 
from bs4 import BeautifulSoup as soup
import requests
import re
import datetime

url ="https://coinmarketcap.com/currencies/ethereum/historical-data/?start=20170906&end=20171006/"

request_for_url = requests.get(url)


soup2parse = soup(request_for_url.text,'lxml')
divs = soup2parse.find_all("div",class_=re.compile("row bottom-margin-1x"))


print(divs[1])