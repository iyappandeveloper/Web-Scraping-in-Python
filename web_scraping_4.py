import requests
from bs4 import BeautifulSoup

url = "https://thehub.io/startups?countryCodes=DK"
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')

title = soup.find('title')
print('\n',title.get_text())
startups = soup.find('div',{'class':'row mt-16 mt-lg-0 mb-16 mb-lg-30'})
print('\n',startups.get_text())
for full in  soup.find_all('div',{'class':'mb-30 col-md-6 col-lg-4'}):
    print('\n',full.get_text())