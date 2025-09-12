import os
import sys
import requests
import time

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

slow_print("        \033[1;35msystem loading......\033[0m")

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
print("""\033[1;36m

███████╗███╗░░░███╗░█████╗░███╗░░██╗
██╔════╝████╗░████║██╔══██╗████╗░██║
█████╗░░██╔████╔██║██║░░██║██╔██╗██║
██╔══╝░░██║╚██╔╝██║██║░░██║██║╚████║
███████╗██║░╚═╝░██║╚█████╔╝██║░╚███║
╚══════╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝
\033[1;33m===================================
\033[1;32mowner      : Atiqul Islam Emon
\033[1;32mFacebook   : atiqulislam8
\033[1;32mWhatsApp   : +1854442-0106
\033[1;33m===================================\033[0m
""")
# Ask the user if they want to start the setup
slow_print("\033[1;36mDo you want to start the IP Track tools..? (y/n):\033[0m")
choice = input()

if choice.lower() == 'y':
    slow_print("\033[1;36m\n[•]Starting  IP lockup...\033[0m")
    
elif choice.lower() == 'n':
    slow_print("\033[1;31m program successfully stoped...\033[0m")

else:
    slow_print("\033[1;31mInvalid input. Please run the script again and enter 'y' or 'n'.\033[0m")
    
def run_ip_program():
    """
    এই ফাংশনটি IP অ্যাড্রেসের তথ্য সংগ্রহ এবং প্রিন্ট করার কাজ করে।
    """
    os.system("clear")

    print("""\033[1;36m
_____                                _
(_____)         _                    | |
   _   ____    | |_   ____ ____  ____| |  _
  | | |  _ \\   |  _) / ___) _  |/ ___) | / )
 _| |_| | | |  | |__| |  ( ( | ( (___| |< (
(_____) ||_/    \\___)_|   \\_||_|\\____)_| \\_)
      |_|
\033[1;33m================================================
\033[1;32mwoner      : Atiqul Islam Emon
\033[1;32mFacebook   : atiqulislam8
\033[1;32mwhatsaap   : +1854442-0106
\033[1;33m================================================\033[0m""")
    ip = input("\033[1;32mEnter Target IP: \033[0m")

    spinner = ['|', '/', '-', '\\']  # Rotating spinner
    print("\033[1;36m[•] Please wite...... \033[0m", end="")

    for _ in range(20):  # number of rotations
        for frame in spinner:
            sys.stdout.write(f"\r\033[1;36m[•] Please wite......{frame}\033[0m")
            sys.stdout.flush()
            time.sleep(0.1)

    try:
        req = requests.get("http://ip-api.com/json/" + ip)
        req.raise_for_status()
        txt = req.json()

        if txt['status'] == 'success':
            print("""\n\n\033[1;32m♡    ∩_∩ 
╭ („• ֊ •„)♡ ┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈╮
     U U Your Ip information here...\033[0m""")
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
            print(f"\n\033[1;33mLive Location: \033[1;36mhttps://www.google.com/maps/place/{txt['lat']},{txt['lon']}\033[0m")
        else:
            print("\n\033[1;31m Invalid IP please enter a valid IP..\033[0m")

    except requests.exceptions.RequestException as e:
        print(f"\n\033[1;31m An error occurred: {e}\033[0m")
        print("\033[1;31mCould not connect to the IP lookup service. Please check your internet connection.\033[0m")

def main():
    """
    এই ফাংশনটি প্রোগ্রামের মূল অংশ, যা প্রথমে ফেসবুক পেজ ভিজিট করার অনুরোধ করে।
    """
    facebook_page_url = "https://www.facebook.com/atiqulislam8"
    
    while True:
        user_input = input("\n\n\033[1;32mFirst follow our Facebook page (y/n)\033[0m : ").lower()
        
        if user_input == 'y':
            print(f"Opening... {facebook_page_url}")
            os.system(f"termux-open-url {facebook_page_url}")
            print("Facebook page opened. Now running the IP lookup program...")
            # ফেসবুক পেজ খোলার পর আইপি প্রোগ্রামটি রান করা হচ্ছে
            run_ip_program()
            break  # প্রোগ্রামটি বন্ধ করার জন্য লুপ থেকে বের হয়ে আসা
            
        elif user_input == 'n':
            slow_print("\n\033[0;31m[⛔] Please wite 10 munite......\033[0m")
            time.sleep(600)
            # সরাসরি আইপি প্রোগ্রামটি রান করা হচ্ছে
            run_ip_program()
            break
            
        else:
            slow_print("\n\033[0;31m[⚠️] Invalid input please enter y or n....\033[0m")

if __name__ == "__main__":
    main()
