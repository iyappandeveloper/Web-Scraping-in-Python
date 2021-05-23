import requests
from bs4 import BeautifulSoup

startups = input("\nEnter your startup company names to scrap the comapany detail\nEx:freshland,lenus-ehealth....\n")
url = "https://thehub.io/startups/"+startups

reg = requests.get(url)
soup = BeautifulSoup(reg.text,'html.parser')

print("\n")
h1 = soup.find('h2')
print("\t\t\t\t\t\t\t",h1.get_text())
print("\n")

for a in soup.find_all('div',{'class':'details__text__content'}):
   print(a.get_text())
print("\n")  

for m in soup.find_all('tr'):
    print("\t\t\t\t\t\t",m.get_text())
print("\n")
