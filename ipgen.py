import random
import ipaddress
from rgbprint import *
def genip():
    while True:
        ip = ipaddress.IPv4Address(random.getrandbits(32))
        if not (ip.is_private or ip.is_loopback or ip.is_multicast or ip.is_reserved):
            return str(ip)

