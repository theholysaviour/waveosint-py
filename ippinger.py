
from rgbprint import *
from os import *

def ping():
    rgbprint("IP or a hostname >># ", color=0x0c5af7, end='')
    ip = input()
    system(f"ping {ip} -n 4")