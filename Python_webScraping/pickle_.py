import json
from bs4 import BeautifulSoup
import requests
import pprint
def pickles():
    url1="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
    all_data=requests.get(url1)
    soup=BeautifulSoup(all_data.text,"html.parser")
    main_div=soup.find('div', class_='_1gX7').span.get_text()
    div1=int(main_div[1:5])
    div2=div1//32+1
    j=1
    n=1
    list1=[]
    data={'positon':'','Name':'','link':'','price':''}
    while j<=div2:
        url2="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471&page="+str(j)
        all_data=requests.get(url2)
        soup=BeautifulSoup(all_data.text,"html.parser")
        name_div=soup.find_all('div', class_='UGUy')
        link_div=soup.find_all('div',class_='_3WhJ')
        price_div=soup.find_all('div', class_='_1kMS')
        
        for i in range(0,len(name_div)):
            data['positon']=n
            data['Name']=name_div[i].get_text()
            data['price']=price_div[i].span.get_text()
            data['link']="https://paytmmall.com//" + link_div[i].a['href']
            list1.append(data)
            data={'positon':'','Name':'','link':'','price':''}
            n+=1
        j+=1
    with open('pickle.json','w') as inside:
        json.dump(list1,inside,indent=4)
        return list1
pprint.pprint(pickles())  