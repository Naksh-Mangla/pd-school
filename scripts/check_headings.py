import re

with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Headings
h_tags = re.findall(r'<(h[1-6])[^>]*>(.*?)</\1>', html, re.I | re.DOTALL)
print("--- HEADINGS ON HOMEPAGE ---")
for tag, text in h_tags:
    clean = ' '.join(re.sub(r'<[^>]+>', ' ', text).split())
    if clean:
        print(f"[{tag.upper()}]: {clean}")

# Check sections or widgets
widgets = re.findall(r'data-widget_type=["\']([^"\']+)["\']', html)
print(f"\nTotal Elementor Widgets on Homepage: {len(widgets)}")
from collections import Counter
for w, c in Counter(widgets).most_common(15):
    print(f"- {w}: {c}")

