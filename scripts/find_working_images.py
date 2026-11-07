import urllib.request
import re
import json

# Let's inspect all images on all pages of the live site and check their HTTP status
with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

urls = re.findall(r'https?://pdpublicschool\.co\.in/wp-content/uploads/[^\"\'\s>]+\.(?:jpg|jpeg|png|webp)', text, re.I)

print(f"Total urls in homepage: {len(set(urls))}")

working = []
for u in set(urls):
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req, timeout=4) as r:
            if r.status == 200:
                working.append(u)
    except Exception as e:
        pass

print(f"Working images: {len(working)}")
for w in sorted(working):
    print(w)

