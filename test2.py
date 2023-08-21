import requests
from bs4 import BeautifulSoup


url = 'https://weather.com/weather/today/l/659c7f88b96953ababfa9edcbfe0f91862a16369756407447207116dfe417462'
var2 = requests.get(url)

if var2 == 200:

   html=var2.content
   soup = BeautifulSoup( html,'html.parser')
   weatherdetails= soup.find('ul',class_='removeIfEmpty')

   if weatherdetails:
      txt=weatherdetails.text
      print (txt)

   else:
      print('details not found')

else :
   print("fetching the data failed")
