import pprint
from bs4 import BeautifulSoup
import requests
import json
url="https://webscraper.io/test-sites"
put=requests.get(url)
soup=BeautifulSoup(put.text,"html.parser")

main_div=soup.find('div', class_='container test-sites')
sub_div=main_div.find_all('div', class_='col-md-7 pull-right')
def ecommerce():
    E_commerce=[]
    position=1
    data={'Position':'','Name':'','Link':''}
    for i in range(0,len(sub_div)):
        data['Position']=position
        data['Name']=sub_div[i].a.get_text().strip()
        data['Link']="https//www.imdb.com" + sub_div[i].a['href']
        E_commerce.append(data.copy())
        position+=1
    with open('E_commerce.json','w') as put:
        json.dump(E_commerce,put,indent=4)
    return E_commerce
pprint.pprint(ecommerce())