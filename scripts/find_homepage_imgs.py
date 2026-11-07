with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

import re
matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', text)
for m in matches:
    if any(k in m.lower() for k in ['about', 'building', 'school', 'cbse', 'pd4', 'pd5', 'pd6', 'pd2']):
        print('HOMEPAGE IMG:', m)

