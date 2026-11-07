import urllib.request
import json
import re

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()

print("--- FETCHING PAGES ---")
pages_raw = fetch('https://pdpublicschool.co.in/wp-json/wp/v2/pages?per_page=100')
pages = json.loads(pages_raw.decode('utf-8'))
print(f"Total Pages: {len(pages)}")
for p in pages:
    print(f"ID: {p['id']} | Title: {p['title']['rendered']} | Slug: {p['slug']} | URL: {p['link']}")

print("\n--- FETCHING POSTS ---")
try:
    posts_raw = fetch('https://pdpublicschool.co.in/wp-json/wp/v2/posts?per_page=100')
    posts = json.loads(posts_raw.decode('utf-8'))
    print(f"Total Posts: {len(posts)}")
    for post in posts:
        print(f"ID: {post['id']} | Title: {post['title']['rendered']} | URL: {post['link']}")
except Exception as e:
    print("Error fetching posts:", e)

print("\n--- FETCHING HOMEPAGE DETAILS ---")
try:
    home_html = fetch('https://pdpublicschool.co.in/').decode('utf-8', errors='ignore')
    print(f"Homepage HTML length: {len(home_html)} chars")
    
    # Check meta tags
    title_match = re.search(r'<title>(.*?)</title>', home_html, re.I)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', home_html, re.I)
    viewport_match = re.search(r'<meta\s+name=["\']viewport["\']\s+content=["\'](.*?)["\']', home_html, re.I)
    print("Title:", title_match.group(1) if title_match else "NONE")
    print("Meta Description:", desc_match.group(1) if desc_match else "NONE")
    print("Viewport:", viewport_match.group(1) if viewport_match else "NONE")
    
    # Stylesheets
    css_files = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']', home_html, re.I)
    print(f"Total CSS stylesheets linked: {len(css_files)}")
    
    # Scripts
    scripts = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', home_html, re.I)
    print(f"Total external scripts: {len(scripts)}")
    
    # Images
    images = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', home_html, re.I)
    print(f"Total images on homepage: {len(images)}")
    
except Exception as e:
    print("Error on homepage:", e)

