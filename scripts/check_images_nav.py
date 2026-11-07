import urllib.request
import json
import re

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()

home_html = fetch('https://pdpublicschool.co.in/').decode('utf-8', errors='ignore')

# 1. Images Analysis
img_matches = re.findall(r'<img([^>]+)>', home_html, re.I)
print(f"Total img tags: {len(img_matches)}")
missing_alt = 0
img_srcs = []
for tag in img_matches:
    alt = re.search(r'alt=["\'](.*?)["\']', tag, re.I)
    src = re.search(r'src=["\'](.*?)["\']', tag, re.I)
    if not alt or not alt.group(1).strip():
        missing_alt += 1
    if src:
        img_srcs.append(src.group(1))

print(f"Images without proper alt text: {missing_alt} out of {len(img_matches)}")

# Check some image sizes
sample_images = list(set([s for s in img_srcs if 'http' in s]))[:10]
print("\nSample image sizes and headers:")
for img_url in sample_images:
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req, timeout=10) as r:
            cl = r.headers.get('Content-Length', 'unknown')
            ct = r.headers.get('Content-Type', 'unknown')
            print(f"- {img_url.split('/')[-1]}: {cl} bytes, type: {ct}")
    except Exception as e:
        print(f"- {img_url.split('/')[-1]}: error {e}")

# 2. Check Navigation Menu Links
print("\n--- MENU / NAVIGATION LINKS ---")
nav_links = re.findall(r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', home_html, re.I | re.DOTALL)
clean_nav = []
for href, text in nav_links:
    text_clean = re.sub(r'<[^>]+>', '', text).strip()
    if text_clean and href not in ['#', 'javascript:void(0)', '']:
        clean_nav.append((href, text_clean))

print(f"Total links on homepage: {len(clean_nav)}")
unique_links = set(clean_nav)
for h, t in sorted(list(unique_links))[:25]:
    print(f"[{t}] -> {h}")

