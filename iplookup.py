import requests
from rgbprint import *
def lookup_ip():
    rgbprint("IP Address >># ", color=0x0c5af7, end='')
    ip_address = input()
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        gradient_print(f" IP: {data['query']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" ISP: {data['isp']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" City: {data['city']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" Region: {data['regionName']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" Country: {data['country']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" Timezone: {data['timezone']}", start_color=0x0c5af7, end_color=0xffffff)
        gradient_print(f" Coordinates: {data['lat']}, {data['lon']}", start_color=0x0c5af7, end_color=0xffffff)
    else:
        rgbprint("IP lookup failed.", color=0xff0000)

