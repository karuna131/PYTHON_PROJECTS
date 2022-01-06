from typing import Sequence, overload
import requests
import json
r="http://api.merakilearn.org/courses"
b=requests.get(r)
b1=b.json()
with open("course.json","w") as h:
    json.dump(b1,h,indent=4)
order = 1
for i in b1:
    print(order,i["name"],i["id"])
    order+=1
course_no=int(input(" enter your course which you want to learn : "))
print(b1[course_no-1]['name'],b1[course_no-1]['id'])
user=("https://api.merakilearn.org/courses/"+str(b1[course_no-1]['id'])+"/exercises")
g=requests.get(user)
b2=g.json()
with open("main.json","w")as j:
    json.dump(b2,j,indent=4)
l1=[]
l2=[]
sec=1
for k in b2["course"]["exercises"]:
    if k["parent_exercise_id"]==None:
        print(sec,k["name"])
        print(" ",1,k["slug"])
        l1.append(k)
        sec+=1
        continue
    if k["parent_exercise_id"]==k["id"]:
        print(sec,k["name"])
        l1.append(k)
        sec+=1
        c=1
    for a in b2["course"]["exercises"]:
        if k["parent_exercise_id"]!=k["id"]:
            print(" ",c,k["name"])
            l2.append(k)
            c+=1
            break
with open("sub.json","w") as v:
    json.dump(l1,v,indent=4)
choose_course=int(input("Enter a course number : "))
for inside in l1:
    if inside["id"]==inside["parent_exercise_id"]:
        print(l1[choose_course-1]["name"])
        w=l1[choose_course-1]["parent_exercise_id"]
        break  
t=1
l3=[]
l4=[]
for ins in range(0,len(l2)):
    if l2[ins]["parent_exercise_id"]==w:
        print(" ",t,l2[ins]["name"])
        l3.append(l2[ins]["name"])
        l4.append(l2[ins]["content"])
        t+=1
choice=int(input("choose a point number from given options : "))
print(l4[choice-1])