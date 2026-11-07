import urllib.request
import re

req = urllib.request.Request('https://pdpublicschool.co.in/', headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req, timeout=10).read().decode('utf-8', errors='ignore')

# Collect all resources (css, js, img)
css_urls = re.findall(r'<link[^>]+rel=["\']stylesheet["\'][^>]+href=["\']([^"\']+)["\']', html)
js_urls = re.findall(r'<script[^>]+src=["\']([^"\']+)["\']', html)
img_urls = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)

print(f"Total CSS files linked: {len(css_urls)}")
print(f"Total JS files linked: {len(js_urls)}")
print(f"Total Image tags: {len(img_urls)}")

def get_total_size(urls):
    total = 0
    errors = 0
    for u in urls[:20]: # sample first 20
        try:
            r = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
            with urllib.request.urlopen(r, timeout=5) as res:
                cl = res.headers.get('Content-Length')
                if cl:
                    total += int(cl)
        except Exception as e:
            errors += 1
    return total, errors

css_size, css_err = get_total_size(css_urls)
js_size, js_err = get_total_size(js_urls)

print(f"Sample 20 CSS files size: {css_size // 1024} KB (Errors: {css_err})")
print(f"Sample 20 JS files size: {js_size // 1024} KB (Errors: {js_err})")

