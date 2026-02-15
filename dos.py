import requests
import random
import threading
from rgbprint import *


def requester():


    with open('resources/UserAgents.txt', 'r') as f:
        user_agents = [line.strip() for line in f if line.strip()]
    gradient_print("URL or IP: ",start_color=0x0c5af7, end_color=0xffffff, end='')
    target_url = input().strip()

    def send_request():
        headers = {"User-Agent": random.choice(user_agents)}
        try:
            response = requests.get(target_url, headers=headers)
            gradient_print(f"Status: {response.status_code}, UA: {headers['User-Agent']}",start_color=0x0c5af7, end_color=0xffffff)
        except Exception as e:
            rgbprint(f"Error: {e}", color=0xff0000)

    try:
        gradient_print("Requests: ",start_color=0x0c5af7, end_color=0xffffff, end='')
        num_threads = int(input())
    except ValueError:
        num_threads = 10

    threads = []

    for _ in range(num_threads):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()