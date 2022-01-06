import json
import random
print()
print("🙏😊...Welcome to Easy and Affordable services...😊🙏")
print()
with open("data.json","r") as h:
    information=json.load(h)
place_list=["khopi khed shivapur","toll plaza","rail way station","flora","katraj","dmart","khopi khed","khopi","khed shivapur","bharti hospital","palasiya","flora institute"]
current_location=input("Enter your Current Locatoin : ")
dropping_point=input("Enter your Dropping Point : ")
def services():
    if current_location in place_list and dropping_point in place_list:
        print()
        random_=random.randint(a=10,b=100)
        print("🛣️ Current location to Drop point distance 🛣️ = ",random_,"km")
        print()
        print("Choose vehicle 🚕 according to your comfort zone ")
        options=["cab 🚗","bike 🏍","Auto 🛺","taxi 🚕"]
        for o in range(0,len(options)):
            print(options[o])
        list1=[]
        select=input("which vehicle you want for going 🚕🛺 : ")
        for j in information:
            if select==information[j]["vehicle"]:
                list1.append(information[j])
        p=1
        for k in list1:
            print(p)
            for l in k:
                print(" ",l,"=",k[l])            
            p+=1
        print()
        select_one=(input("Select one Driver name : "))
        for k in list1:
            if select_one==k["driver"]:
                print("Contact Number 📲 : ",k["Contect_number"])
                print("vehical Number : ",k["vehical_number"])
                print("Driver current location : ",random.choice(place_list))
                print()
                print("For that you will pay ",k["amount/km"]*random_)
                print()
        yes_or_not=input("you want to book yes or not : ")
        if yes_or_not=="yes":
            print()
            otp=6543
            print("okey your genreted otp is.. ",otp)
            enter_otp=int(input("Enter your genreted otp : "))
            if  otp==enter_otp:
                print("your otp is succesfully verified 😊")
                print()
                print("What you will prefer for payment 💵")
                payment=input("online or cash : ")
                if payment=="online":
                    print("From which way you want to do payment 'Google pay','PhonePe','Paytm','QR code'")
                    print()
                    payment_way=input("payment by : ")
                    print("payment succesfull 🥳👍")
                else:
                    print("pay to driver ")
            else: 
                print("otp is not currect")
        else:
            print("Thank you for coming 🙏😊")
        feedback=input("Give Rating ***** : ")
        if feedback=="*" or feedback=="**":
            print("bad  👎😔")
        elif feedback=="***":
            print("good 👍")
        elif feedback=="****":
            print("very good 👍👍")
        elif feedback=="*****":
            print("awesome 👌👍")
        else:
            print("Excellent  👌👌")
    else:
        print("on this location we are not providing our services")
services()