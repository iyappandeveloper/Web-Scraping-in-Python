import requests
from bs4 import BeautifulSoup

url = "https://thehub.io/startups/freshland"          
reg = requests.get(url)
soup = BeautifulSoup(reg.text,'html.parser')

title = soup.find('h2')
content =  soup.find('div',{'class':'details__text__content'})
detail = soup.find('div',{'class':'details__info col-lg-5'})
linkdin = soup.find('section',{'class':'mb-30 component-container component-container--width--medium component-container--spacing--medium component-container--border-top'})
options = soup.find('section',{'class':'component-container component-container--width--medium component-container--spacing--default'})

freshland = {
    'Title':title.get_text(),
    'content':content.get_text(),
    'details':detail.get_text(),
    'linkdin_profile':linkdin.get_text(),
    'options':options.get_text()
    
}
print(freshland["linkdin_profile"])




