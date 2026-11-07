import urllib.request
import re

def check(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req, timeout=8).read().decode('utf-8', errors='ignore')
    imgs = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', html)
    print(f"=== {url} ===")
    for img in imgs:
        if 'uploads' in img:
            print(" ", img)

check('https://pdpublicschool.co.in/about-us/')
check('https://pdpublicschool.co.in/infrastructure/')

