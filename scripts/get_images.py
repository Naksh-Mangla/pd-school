import re

with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

imgs = re.findall(r'https?://pdpublicschool\.co\.in/wp-content/uploads/[^\"\'\s>]+', html)
print('Found upload images:', len(imgs))
real_imgs = []
for u in set(imgs):
    if any(ext in u.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp']):
        real_imgs.append(u)
        print('-', u)

