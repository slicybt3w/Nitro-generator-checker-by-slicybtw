#Imports
import os
import re
from colorama import Fore ,init ,Style ,Back
from discord.ext import commands
import discord 
import random 
import keep_alive
import string
import time
import requests ,os ,sys ,random ,os .path ,time
import ctypes
init()
current_path =os .path .dirname (os .path .realpath (__file__ ))
print(Fore.BLUE + "hosting alive on port 8080")
print(Fore.GREEN + """
███╗░░██╗██╗████████╗██████╗░░█████╗░░░░░░░░██████╗░██╗███████╗████████╗
████╗░██║██║╚══██╔══╝██╔══██╗██╔══██╗░░░░░░██╔════╝░██║██╔════╝╚══██╔══╝
██╔██╗██║██║░░░██║░░░██████╔╝██║░░██║█████╗██║░░██╗░██║█████╗░░░░░██║░░░
██║╚████║██║░░░██║░░░██╔══██╗██║░░██║╚════╝██║░░╚██╗██║██╔══╝░░░░░██║░░░
██║░╚███║██║░░░██║░░░██║░░██║╚█████╔╝░░░░░░╚██████╔╝██║██║░░░░░░░░██║░░░
╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░░░╚═════╝░╚═╝╚═╝░░░░░░░░╚═╝░░░
░██████╗░███████╗███╗░░██╗███████╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔════╝░██╔════╝████╗░██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░██╗░█████╗░░██╔██╗██║█████╗░░██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░╚██╗██╔══╝░░██║╚████║██╔══╝░░██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚██████╔╝███████╗██║░╚███║███████╗██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚══════╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
░░██╗░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
╚═██╔═╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
░░╚═╝░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
░░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
#print nitro gift generator + checker
time.sleep(2)
print(Fore.GREEN + "made by: slicybtw")
os.system("cls")
time.sleep(2)
print(Fore.BLUE + "Creator yt channel: slicybtw")
discord = requests.get('https://cdn.sourceb.in/bins/ZuFjpdCQ8D/0')
print(Fore.YELLOW + discord.text + ' JOIN OR NO NITRO')
yt = requests.get("https://cdn.sourceb.in/bins/scktwiJRKv/0") 
print(Fore.GREEN + yt.text + "SUB OR NO NITRO")
time.sleep(1)
print(Fore.GREEN+ 'Input how many codes to generate')
num = int(input(''))
# input for nitro
f=open("Nitro Codes.txt","w", encoding='utf-8')
#save all the codes to Nitro Codes.txt

print("Wait, Generating for you!")
for n in range(int(num)):
   y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(19))
   f.write('https://discord.gift/')
   f.write(y)
   f.write("\n")

f.close()
#generate the nitro 

#=============Checker=========================


with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v7/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(Fore.GREEN + " Valid | {} ".format(line.strip("\n")))
            file = open("valid.txt")
            #open valid.txt for valid codes 
            valid = [] #tracks how many valid Codes
            break
        else:
        	print(Fore.RED + " Invalid | {} ".format(line.strip("\n")))
        	Invalid = 0
        	
        	
        	 
input("program ended enter to exit")
#codes written by slicybtw yt channel slicybtw 