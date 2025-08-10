import os,sys,time,requests



# Function to print text with a typing effect
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

def clear_screen():
    os.system("clear")

clear_screen()
print("\n\n\n")

slow_print("        system loading......")

print("\n\n\n")
time.sleep(2)
clear_screen()
print("\n\n")

slow_print("        \033[1;32msuccessfully loaded\n", delay=0.05)

name = input("        \033[1;34mEnter your name: \033[0m")
slow_print(f"        \033[1;33mHello \033[1;32m{name}, \033[1;33mwelcome to my new tools..")

print("\n\n")
time.sleep(2)
clear_screen()




os.system("clear")

print("""\033[1;36m
  _____    _______             _             
 |_   _|  |__   __|           | |            
   | |  _ __ | |_ __ __ _  ___| | _____ _ __ 
   | | | '_ \| | '__/ _` |/ __| |/ / _ \ '__|
  _| |_| |_) | | | | (_| | (__|   <  __/ |   
 |_____| .__/|_|_|  \__,_|\___|_|\_\___|_|   
       | |                                   
       |_|                                   
\033[1;33m===================================
\033[1;32mwoner      : Atiqul Islam Emon
\033[1;32mFacebook   : atiqulislam8
\033[1;32mwhatsaap   : +1854442-0106
\033[1;33m===================================\033[0m""")
ip = input("\033[1;32mEnter Target IP: \033[0m")

req = requests.get("http://ip-api.com/json/" + ip)
txt = req.json()

#sms
spinner = ['|', '/', '-', '\\']  # Rotating spiner
print("\033[1;36m[•] Please wite...... \033[0m", end="")

for _ in range(20):  #number of rotations
    for frame in spinner:
        sys.stdout.write(f"\r\033[1;36m[•] Please wite......{frame}\033[0m")
        sys.stdout.flush()
        time.sleep(0.1)

if txt['status'] == 'success':
    print("""\n\033[1;32m♡    ∩_∩ 
╭ („• ֊ •„)♡ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
     U U Your Ip informstion here...\033[0m""")
    print(f"\033[1;33mIP Address   : \033[1;36m{txt['query']}\033[0m")
    print(f"\033[1;33mCountry      : \033[1;36m{txt['country']} ({txt['countryCode']})\033[0m")
    print(f"\033[1;33mRegion       : \033[1;36m{txt['regionName']} ({txt['region']})\033[0m")
    print(f"\033[1;33mCity         : \033[1;36m{txt['city']}\033[0m")
    print(f"\033[1;33mZIP Code     : \033[1;36m{txt['zip']}\033[0m")
    print(f"\033[1;33mLat          : \033[1;36m{txt['lat']}\033[0m")
    print(f"\033[1;33mLon          : \033[1;36m{txt['lon']}\033[0m")
    print(f"\033[1;33mTimezone     : \033[1;36m{txt['timezone']}\033[0m")
    print(f"\033[1;33mISP          : \033[1;36m{txt['isp']}\033[0m")
    print(f"\033[1;33mOrganization : \033[1;36m{txt['org']}\033[0m")
    print(f"\033[1;33mAS Info      : \033[1;36m{txt['as']}\033[0m")
    print(f"\n\033[1;33mLive Location: \033[1;36mhttps://www.google.com/maps/search/?api=1&query={txt['lat']},{txt['lon']}\033[0m")
else:
    print("\033[1;31m Invalid IP please enter a valid IP..\033[0m")
