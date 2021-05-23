import requests
from bs4 import BeautifulSoup

pages=input("\nEnter your website page number title scrap\nEx:1,2,3,4,5,6............\n")

url = "https://thehub.io/startups?countryCodes=DK&page="+pages
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
print("\n")

title = soup.find('title')
print(title.get_text())
print("\n")

print("\t\tstartups:\n")
for a in soup.find_all('h4'):
    print(a.get_text())

print("\n")
