from rgbprint import *
from usersearch import userlookup
import getpass
from time import *
from ippinger import ping
from ipgen import genip
from iplookup import lookup_ip
from dos import requester
import os

import requests
username = getpass.getuser()





def main():
    gradient_print(
        """
                        ██╗    ██╗ █████╗ ██╗   ██╗███████╗ ██████╗ ███████╗██╗███╗   ██╗████████╗
                        ██║    ██║██╔══██╗██║   ██║██╔════╝██╔═══██╗██╔════╝██║████╗  ██║╚══██╔══╝
                        ██║ █╗ ██║███████║██║   ██║█████╗  ██║   ██║███████╗██║██╔██╗ ██║   ██║   
                        ██║███╗██║██╔══██║╚██╗ ██╔╝██╔══╝  ██║   ██║╚════██║██║██║╚██╗██║   ██║   
                        ╚███╔███╔╝██║  ██║ ╚████╔╝ ███████╗╚██████╔╝███████║██║██║ ╚████║   ██║   
                         ╚══╝╚══╝ ╚═╝  ╚═╝  ╚═══╝  ╚══════╝ ╚═════╝ ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
        """, 
        start_color=0x0c5af7, 
        end_color=0xe5eeff
    )

    gradient_print(
        """
                            ═════════════════════════════════════════════════════════════════
                            ║                     made by theholysave <3                    ║
                            ║           with great tools comes great responsobility         ║
                            ║                                                               ║
                            ║     [01] Phone number           [08] Username Lookup          ║
                            ║     [02] Full name              [09] IP generator (random)    ║
                            ║     [03] Credit card            [10] Shitty Ddoser            ║
                            ║     [04] IP Lookup                                            ║
                            ║     [05] Email Lookup                                         ║
                            ║     [06] IP Pinger                                            ║
                            ║     [07] Paste Creator                                        ║
                            ║                                                               ║
                            ║     [00] Exit                                                 ║
                            ═════════════════════════════════════════════════════════════════
                """,
                start_color=0x0c5af7,
                end_color=0xe5eeff

    )




    while True:
        gradient_print(f"┌──{username}@waveosint /menu", start_color=0x0c5af7,end_color=0xffffff)
        rgbprint("└─# ", color=0x0c5af7, end='')
        choice = input()
        if choice == '00':
            exit()

        if choice == '04':
            lookup_ip()


        if choice == '06':
            ping()
        
        if choice == '08':
            userlookup()

        if choice == '09':
            gradient_print(genip(), start_color=0x0c5af7, end_color=0xe5eeff)

        if choice == '10':
            requester()

try:
    req = requests.get("http://localhost:3000/a7dffhg7asdjhas82293hds7312fgd631s.txt")
    server_key = [line.strip() for line in req.text.splitlines() if line.strip()]
except requests.exceptions.RequestException as e:
    print("Failed to connect to server:", e)
    exit()

while True:
    key = input("key: ").strip()
    if key in server_key:
        rgbprint("access granted", color=0x00ff0f)
        sleep(1)
        os.system("cls")
        main()
        break
    else:
        rgbprint("access denied", color=0xff0000)
        sleep(3)
        os.system("cls")