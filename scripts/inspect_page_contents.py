import urllib.request
import json
import re

# Let's inspect the actual content rendered in the main area of pages
def get_main_content(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            # Extract title
            title = re.search(r'<title>(.*?)</title>', html, re.I)
            title_text = title.group(1) if title else url
            
            # Extract elementor or article content
            # Remove scripts and styles
            clean_html = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', html, flags=re.DOTALL | re.I)
            
            # Find main text
            text = re.sub(r'<[^>]+>', ' ', clean_html)
            text = ' '.join(text.split())
            
            # Find all links
            links = re.findall(r'href=["\'](http[s]?://pdpublicschool\.co\.in/[^"\']*)["\']', html)
            
            return {
                'title': title_text,
                'length': len(html),
                'text_sample': text[text.find('Skip to content') if 'Skip to content' in text else 0:text.find('Skip to content') + 600 if 'Skip to content' in text else 600],
                'links_count': len(links),
                'pdf_links': [l for l in re.findall(r'href=["\']([^"\']+\.pdf)["\']', html, re.I)]
            }
    except Exception as e:
        return {'error': str(e)}

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
    'https://pdpublicschool.co.in/from-principal-desk/'
]

for u in urls:
    res = get_main_content(u)
    print(f"\n--- URL: {u} ---")
    if 'error' in res:
        print("Error:", res['error'])
    else:
        print("Title:", res['title'])
        print("PDF links found:", res['pdf_links'])
        print("Sample Text:", res['text_sample'][:250])
