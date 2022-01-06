import json
import re
import os
file=os.path.exists("loginSignup.json")
print(file)
if file==False:
  
    dic2={}
    list1=[] 
    dic1={}
    user=input("what you want Signup or Login : ")
    if user=="signup":
        name=input("Enter your name : ")
        password1=input("Enter your password : ")
        if re.search("[A-Z]",password1) and re.search("[a-z]",password1) and re.search("[0-9]",password1) and re.search("[@#$&]",password1):
            password2=input("Conform your password : ")
            if password1==password2:
                print("Congrats ",name)
                description=input("Enter a Description : ")
                birth=input("Enter your DOB : ")
                hobby=input("Enter your Hobbies : ")
                Gender=input("Enter your Gender F/M : ")
                l1=["Name","Password","describtion","DOB","Hobbies","Gender"]
                l2=[name,password2,description,birth,hobby,Gender,]
                
                for i in range(0,len(l1)):
                    dic2.update({l1[i]:l2[i]})
                
                list1.append(dic2)
                dic1.update({password2:list1})
                with open("loginSignup.json", "w") as injson:
                    json.dump(dic1,injson,indent=4)
            else:
                print("both password are not same")
        else:
            print("your password is not strong,try again")        
elif file==True:
    list1=[]
    user=input("what you want Signup or Login : ")
    if user=="signup":
        name=input("Enter your name : ")
        password1=input("Enter your password : ")
        with open("loginSignup.json","r") as h:
            data=json.load(h)
        if re.search("[A-Z]",password1) and re.search("[a-z]",password1) and re.search("[0-9]",password1) and re.search("[@#$&]",password1):
            password2=input("Conform your password : ")
            if password1==password2:
                print("Congrats ",name)
                description=input("Enter a Description : ")
                birth=input("Enter your DOB : ")
                hobby=input("Enter your Hobbies : ")
                Gender=input("Enter your Gender F/M : ")
                print("congrats ",name,"you have succesfully signup")
                l1=["Name","Password","describtion","DOB","Hobbies","Gender"]
                l2=[name,password2,description,birth,hobby,Gender,]
                dic2={}
                for i in range(0,len(l1)):
                    dic2.update({l1[i]:l2[i]}) 
                
                list1.append(dic2)
                data.update({password2:list1})
                with open("loginSignup.json", "w") as injson:
                    json.dump(data,injson,indent=4)
            else:
                print("both password are not same")
        else:
            print("your password is not strong,try again")        
    elif user=="login":
        user_name=input("Enter user name : ")
        user_password=input("Enter your password : ")
        with open("loginSignup.json","r") as h:
            data=json.load(h)
        for i in data:
            if i==user_password:
                print("your given information is correct")
                print(data[i])
                break
        else:
            print("sorry your password is wrong")