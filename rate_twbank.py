from bs4 import BeautifulSoup as soup
import requests
import re
import datetime
tw_bank = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
url_data = requests.get(tw_bank)
soup2parse = soup(url_data.text,'html.parser')

divs = soup2parse.find_all("div",class_=re.compile("visible-phone print_hide"))
#print(divs)
#現金匯率 rate-content-cash text-right print_hide
#即期匯率 rate-content-sight text-right print_hide hidden-phone
#div_dollar = soup2parse.find_all("td",class_=re.compile("rate-content-cash text-right print_hide"))

#for index , element in enumerate(div_dollar):
    #print(re.findall(r'[0-9]{1,3}.[0-9]{1,7}',element.text))







#print(re.findall(r'[0-9]\w[0-9]',div_dollar))
#usd = []
#divs = soup2parse.select("tbody")
#for index,element in enumerate(divs):
    #print(index)
   # usd.append(re.findall(r'[A-Z]{3}',element.text))
#print(usd)
#print(divs)

#time_today = re.findall(r'[0-9]{4}/[0-9]{2}/[0-9]{2}',divs[0].text)


#print(time_today)


#print(regex_format)





class crawl_twbank:
    def __init__(self):
        self.homepage = "http://rate.bot.com.tw/xrt?Lang=zh-TW"
        self.rate = {}
        
    def rate(self):
        soup = BeautifulSoup()
    def check_status(self):
        try:
            page = requests.get(self.homepage)
            if page.status_code == "200":
                soup_find = soup(page)
                print(soup_find.p['id'])
        except:
            pass
    def find_cash_rate(self):
        url_data = requests.get(tw_bank)
        soup2parse = soup(url_data.text,'html.parser')
        #找title
        dollar_date = soup2parse.select("span.time")
        title=""
        if isinstance(dollar_date,list):
            date_index = re.findall(r'[0-9]{4}/[0-9]{2}/[0-9]{2}',dollar_date[0].text)
            title = date_index[0]
        else:
            title = datetime.datetime.today().strftime('%Y/%m/%d')

        #找幣別
        divs = soup2parse.find_all("div",class_=re.compile("hidden-phone print_show"))
        currency=[]
        if isinstance(divs,list):
            for index,element in enumerate(divs):
                currency_element = re.findall(r'[A-Z]{3}',element.text)
                if not len(element) == 0 :
                    currency.append(currency_element[0])
                else:
                    currency = None
        else:
            usd= None 
        #找匯率
        
        rates=[]
        div_rates = soup2parse.find_all("td",class_=re.compile("rate-content-cash text-right print_hide"))
        if isinstance(div_rates,list):        
            for index , element in enumerate(div_rates):
                rate = re.findall(r'[0-9]{1,3}.[0-9]{0,7}',element.text)
                if len(rate) == 0 :
                    rates.append('0')
                else :
                    rates.append(rate[0])
        else:
            rates = None  
        all_rate_fisrt={}
        all_rate = {}
        if not title is None :
            if isinstance(currency,list):
                    
                for index,element in enumerate(currency): 
                    all_rate[element] = [rates[index * 2],rates[index * 2+1]]        
            
            all_rate_fisrt[title] = all_rate
        return all_rate_fisrt
#a = crawl_twbank()

#b = a.find_cash_rate()
#print(b)

