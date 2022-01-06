from bs4 import BeautifulSoup
import requests
import pprint
import json
url="https://www.imdb.com/india/top-rated-indian-movies/"
res = requests.get(url)
soup=BeautifulSoup(res.text, 'html.parser')
def scrape_top_list():
    main_div=soup.find('div', class_='lister')
    tbody=main_div.find('tbody', class_='lister-list')
    trs=tbody.find_all('tr')

    movie_rank=[]
    movie_name=[]
    year_of_realease=[]
    movie_url=[]
    movie_ratings=[]
    
    for tr in trs:
        rank=1
        for i in trs:
            rank=rank+1
        movie_rank.append(rank)  
        title=tr.find("td", class_="titleColumn").a.get_text()
        movie_name.append(title)

        year=tr.find("td", class_="titleColumn").span.get_text()
        year_of_realease.append(year)

        imdb_rating=tr.find("td", class_="ratingColumn imdbRating").strong.get_text()
        movie_ratings.append(imdb_rating)

        link=tr.find("td",class_="titleColumn").a["href"]
        movie_link = "https//www.imdb.com" + link
        movie_url.append(movie_link)
        
    top_movies=[]
    details={"position":"","name":"","year":"","rating":"","url":""}
    for i in range(0,len(movie_rank)):
        details["position"]=int(movie_rank[i])
        details["name"]=str(movie_name[i])
        year_of_realease[i]=year_of_realease[i][1:5]
        details["year"]=int(year_of_realease[i])
        details["rating"]=float(movie_ratings[i])
        details["url"]=movie_url[i]
        top_movies.append(details)
        details={"position":"","name":"","year":"","rating":"","url":""}
    return top_movies
s=scrape_top_list()

def group_by_year(movies):
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
    with open("web.json","w") as h:
        json.dump(dic,h,indent=4)
    return dic
s1=(group_by_year(s))

def group_by_decade(movies):
    moviedec={}
    list2=[]
    for index in movies:
        mod=index%10
        decade=index-mod
        if decade not in list2:
            list2.append(decade)
    list2.sort()
    for i in list2:
        moviedec[i]=[]
    for i in moviedec:
        dec10 = i+9
        for x in movies:
            if x<=dec10 and x>=i:
                for v in movies[x]:
                    moviedec[i].append(v)
    return moviedec
pprint.pprint(group_by_decade(s1))               