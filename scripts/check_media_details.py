import urllib.request
import json

# Check the media objects for these images
req = urllib.request.Request('https://pdpublicschool.co.in/wp-json/wp/v2/media?per_page=100', headers={'User-Agent': 'Mozilla/5.0'})
media = json.loads(urllib.request.urlopen(req, timeout=10).read().decode('utf-8'))

for m in media:
    url = m.get('source_url', '')
    title = m.get('title', {}).get('rendered', '')
    desc = m.get('description', {}).get('rendered', '')
    caption = m.get('caption', {}).get('rendered', '')
    if any(k in url.lower() for k in ['pd6', 'dsc_9009', 'dsc_7609', 'img_3032', 'img_2997', 'whatsapp-image-2025']):
        print(f"TITLE: {title} | CAPTION: {caption} | URL: {url}")

