import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
url="https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/"
r=requests.get(url)
soup=BeautifulSoup(r.text,"html.parser")

main_class=soup.find('table', class_='table')
position_list=main_class.find_all('td',class_='bold')
rating_list=main_class.find_all('span', class_='tMeterScore')
name_list=main_class.find_all('a',class_='unstyled articleLink')
review_list=main_class.find_all('td',class_='right hidden-xs')
link_list=main_class.find_all('a',class_='unstyled articleLink')

def movies():           # Task 1
    data_list=[]
    data={'position':'','Link':'','rating':'','name':'','review':'','year':''}
    for i in range(0,len(position_list)):
        data['position']=position_list[i].get_text()
        data['rating']=rating_list[i].get_text().strip()
        data['Link']="https://www.rottentomatoes.com/"+link_list[i]['href']
        data['name']=name_list[i].get_text().strip()
        a=data['name'].split("(")
        data['year']=int(a[-1][0:5-1])
        data['review']=review_list[i].get_text()
        data_list.append(data.copy())
    with open('top_movies.json','w') as task1:
        json.dump(data_list,task1,indent=4)
    return data_list
#pprint(movies())
s=movies()
def group_by_year(movies):              # Task 2
    years=[]
    dic={}
    for i in movies:
        year=i["year"]
        if year not in years:
            years.append(year)
    for j in years:
        list1=[]
        for k in movies:
            if j==k["year"]:
                list1.append(k)
            dic.update({j:list1})
    with open("top_movies_yearGroup.json","w") as task2:
        json.dump(dic,task2,indent=4)
    return dic
#pprint(group_by_year(s))
s1=group_by_year(s)

def year10_gap_group(movies):                   # Task 3
    moviesdec={}
    list2=[]
    for i in movies:
        mod=i%10
        decade=i-mod
        if  decade not in list2:
            list2.append(decade)
    list2.sort()
    for i in list2:
        moviesdec[i]=[]
    for i in moviesdec:
        dec10=i+9
        for x in movies:
           if x<=dec10 and x>=i:
                for k in movies[x]:
                    moviesdec[i].append(k)
    with open("year10_gap_group.json","w") as task3:
        json.dump(moviesdec,task3,indent=4)
    return moviesdec
# pprint(year10_gap_group(s1))  
s2=year10_gap_group(s1)     

def movie_link_data(Movie_Url):                 # Task 4
    movie_position=input("Enter any movie position : ")
    for i in Movie_Url:
        if i['position']==movie_position:
            extract_link=str(i['Link'])
            res=requests.get(extract_link)
            soup_=BeautifulSoup(res.text,"html.parser")
            main_li=soup_.find_all('li',class_='meta-row clearfix')
            key_div=soup_.find_all('div', class_='meta-label subtle')
            value_div=soup_.find_all('div',class_='meta-value')
            dic={}
            list3=[]
            for j in range(0,len(main_li)):
                key=key_div[j].get_text().strip()
                value=value_div[j].get_text().strip()
                dic.update({key:value})
                if key=='Genre:' or 'Director:' or 'Producer:' or 'Original Language:' or 'Production Co:':
                    sp_value=value.split()
                    list3.append(sp_value)
                    dic.update({key:list3})
                else:
                    dic.update({key:value})
            pprint(dic)
            #pprint(dic)
movie_link_data(s)