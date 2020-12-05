# IPLocation

import socket
import os
import requests
import sys
import time
from colorama import Fore

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
        print(target)
        info = requests.get("https://api.hackertarget.com/ipapi/?q=" + target).text
        if info.status_code == 404:
            print("Ok    KKKKKKKKKKKKKKKKKKKK")
__1__()           
