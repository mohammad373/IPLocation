# IPLocation

import socket
import os
import requests
import sys
import time
from Colorama import Fore

def __1__():
    try:
        print(Fore.GREEN + "Hello . I`m Hacker Nwwb ;)")
        site = input(Fore.RED + "Enter Your Address WebSite" + Fore.YELLOW + " ==>  ")
        if site == "":
            try:
                print(Fore.GREEN + "Ok Good Lunch " + Fore.RED + ";) ")
                time.sleep(2)
                os.system("clear")
            except:
                pass
        if not "http" in site or not "https" in site:
            site = "http://" + site
        target = socket.gethostbyname(str(site))
        info = requests.get("https://www.iplocation.net" + target).text
        print(info)
    except:
        try:
            print(Fore.RED + "Ok Good Bay ;)")
            os.system("clear")
        except:
            pass
__1__()
