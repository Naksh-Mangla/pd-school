import urllib.request
import re
import json

def fetch_text(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            clean = re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.I)
            text = re.sub(r'<[^>]+>', ' ', clean)
            return ' '.join(text.split()), html
    except Exception as e:
        return f"Error: {e}", ""

pages = [
    ('Home', 'https://pdpublicschool.co.in/'),
    ('Admission', 'https://pdpublicschool.co.in/admission-procedure/'),
    ('Fee Structure', 'https://pdpublicschool.co.in/fee-structure/'),
    ('Circular', 'https://pdpublicschool.co.in/circular/'),
    ('Career', 'https://pdpublicschool.co.in/career/'),
    ('Contact', 'https://pdpublicschool.co.in/contact-us/'),
    ('Staff', 'https://pdpublicschool.co.in/staff/'),
    ('Gallery', 'https://pdpublicschool.co.in/gallery/'),
    ('Video Gallery', 'https://pdpublicschool.co.in/video-gallery/')
]

for name, u in pages:
    txt, raw = fetch_text(u)
    print(f"=== {name} ({u}) ===")
    print("Content preview (first 500 chars):")
    print(txt[:500])
    # Check if there are tables, forms, or images
    tables = len(re.findall(r'<table', raw, re.I))
    forms = len(re.findall(r'<form', raw, re.I))
    imgs = len(re.findall(r'<img', raw, re.I))
    inputs = re.findall(r'<input[^>]+type=[\"\'](.*?)[\"\']', raw, re.I)
    print(f"Tables: {tables}, Forms: {forms}, Images: {imgs}, Input types: {set(inputs)}")
    print()

