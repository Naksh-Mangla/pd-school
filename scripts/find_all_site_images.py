import urllib.request
import re
import json

urls = [
    'https://pdpublicschool.co.in/',
    'https://pdpublicschool.co.in/about-us/',
    'https://pdpublicschool.co.in/admission-procedure/',
    'https://pdpublicschool.co.in/fee-structure/',
    'https://pdpublicschool.co.in/contact-us/',
    'https://pdpublicschool.co.in/career/',
    'https://pdpublicschool.co.in/circular/',
    'https://pdpublicschool.co.in/mandatory-public-disclosures/',
    'https://pdpublicschool.co.in/staff/',
    'https://pdpublicschool.co.in/gallery/',
    'https://pdpublicschool.co.in/video-gallery/',
    'https://pdpublicschool.co.in/directors-desk/',
    'https://pdpublicschool.co.in/from-principal-desk/',
    'https://pdpublicschool.co.in/infrastructure/',
    'https://pdpublicschool.co.in/transportation-facility/',
    'https://pdpublicschool.co.in/outline/',
    'https://pdpublicschool.co.in/intra-school-competition/'
]

all_images = set()

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as r:
            html = r.read().decode('utf-8', errors='ignore')
            found = re.findall(r'https?://pdpublicschool\.co\.in/wp-content/uploads/[^\"\'\s>]+\.(?:jpg|jpeg|png|webp)', html, re.I)
            for img in found:
                # filter out thumbnails like 150x150, 300x200 if original or larger exists
                all_images.add(img)
    except Exception as e:
        print(f"Error on {u}: {e}")

print(f"Total unique images found across the whole website: {len(all_images)}")

# Group images by base filename
base_images = {}
for img in all_images:
    filename = img.split('/')[-1]
    # Check if thumbnail
    clean_name = re.sub(r'-\d+x\d+', '', filename)
    if clean_name not in base_images:
        base_images[clean_name] = []
    base_images[clean_name].append(img)

print("\n--- BASE IMAGES ---")
for k, v in sorted(base_images.items()):
    # pick highest resolution
    print(f"Image: {k} (variants: {len(v)}) -> {v[-1]}")

