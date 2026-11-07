import urllib.request
import ssl

ctx = ssl.create_default_context()
req = urllib.request.Request('https://pdpublicschool.co.in/', headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req, context=ctx) as resp:
    print("--- HEADERS ---")
    for k, v in resp.headers.items():
        print(f"{k}: {v}")

