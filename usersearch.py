import requests
from rgbprint import *



def userlookup():
    rgbprint("username >># ", color=0x0c5af7, end='')
    user = input()
    urls = [
        f"https://www.1337x.to/user/{user}",
        f"https://2Dimensions.com/a/{user}",
        f"https://www.7cups.com/@{user}",
        f"https://www.9gag.com/u/{user}",
        f"https://apclips.com/{user}",
        f"https://about.me/{user}",
        f"https://independent.academia.edu/{user}",
        f"https://admireme.vip/{user}",
        f"https://airbit.com/{user}",
        f"https://www.allthingsworn.com/profile/{user}",
        f"https://allmylinks.com/{user}",
        f"https://www.roblox.com/user.aspx?username={user}",
        f"https://osu.ppy.sh/users/{user}",
        f"https://steamcommunity.com/id/{user}",
        f"https://onlyfans.com/{user}",
        f"https://fansly.com/{user}",
        f"https://manyvids.com/Profile/{user}",
        f"https://www.pornhub.com/users/{user}",
        f"https://xvideos.com/profiles/{user}",
        f"https://xhamster.com/users/{user}",
        f"https://www.manyvids.com/Profile/{user}",
        f"https://soundcloud.com/{user}",
        f"https://ko-fi.com/{user}",
        f"https://patreon.com/{user}",
        f"https://imgur.com/user/{user}",
        f"https://canva.com/{user}",
        f"https://github.com/{user}",
        f"https://gitlab.com/{user}"
    ]
    
    
    
    

    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            if res.status_code == 200:
                gradient_print(f"[+] Found: {url}", start_color=0x0c5af7, end_color=0xe5eeff)
            elif res.status_code == 404:
                gradient_print(f"[-] Not found: {url}", start_color=0x0c5af7, end_color=0xe5eeff)
            else:
                gradient_print(f"[?] {url} returned status {res.status_code}", start_color=0x0c5af7, end_color=0xe5eeff)
        except requests.RequestException as e:
            gradient_print(f"[!] Error checking {url}: {e}", start_color=0x0c5af7, end_color=0xe5eeff)
            
