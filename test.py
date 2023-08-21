import requests
from bs4 import BeautifulSoup



url = 'https://sleepobrace.com/'
response = requests.get(url)
html1=response.text

#html content of the page is in html1 var now
#we need to parse it using beautiful soup

soup = BeautifulSoup(html1,'html.parser')
bookel= soup.find_all('div',class_='container')

for x in bookel:
    p=x.find('p' )
    print(p)