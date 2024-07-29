import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL to make the GET request to
url = 'https://www.etmoney.com/stocks/list-of-stocks'

# Define the User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Make the GET request with the User-Agent header
response = requests.get(url, headers=headers).text

soup = BeautifulSoup(response,'lxml')

company=[]
CurrentPrice=[]
high_low=[]
MarketCap=[]
Industry=[]

tbody=soup.find('tbody')
for tr in tbody:
    
    for index,td in enumerate(list(tr)):
        
        if index==0:
            string = td.find('a').text.strip()
            company.append(string[:string.find('.')+1])
        elif index==1:
            string = td.find('span').text.strip()
            CurrentPrice.append(string[:string.find(' ')+1])

        elif index==2:
            high_low.append(td.find('span').text.strip())

        elif index==3:
            MarketCap.append(td.find('span').text.strip())

        else:
             Industry.append(td.find('span').text.strip())


df = pd.DataFrame({"company":company,"CurrentPrice":CurrentPrice,"high_low":high_low,"MarketCap":MarketCap,"Industry":Industry})
print(df)