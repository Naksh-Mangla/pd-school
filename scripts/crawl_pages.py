import urllib.request
import json
import re

pages_raw = open('pages.json', 'r', encoding='utf-8').read()
pages = json.loads(pages_raw)

print(f"Total pages to audit: {len(pages)}")

for p in pages:
    url = p['link']
    title = p['title']['rendered']
    print(f"\n==============================")
    print(f"Auditing: {title} ({url})")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            status = resp.status
            # Find broken links on this page
            links = re.findall(r'href=["\']([^"\']+)["\']', html)
            # Find forms
            forms = re.findall(r'<form([^>]*)>', html)
            # Find text length
            body_text = re.sub(r'<[^>]+>', ' ', html)
            body_text = ' '.join(body_text.split())
            
            print(f"Status: {status} | Forms: {len(forms)} | Content length: {len(body_text)} chars")
            
            # Check for dummy/template content like 'Lorem ipsum'
            lorem = re.findall(r'lorem\s+ipsum', html, re.I)
            if lorem:
                print(f"WARNING: Contains {len(lorem)} instances of 'Lorem Ipsum' placeholder text!")
                
            # Check for specific school details
            if 'career' in url.lower():
                print("Career Page snippet:", body_text[:300])
            elif 'fee' in url.lower():
                print("Fee Page snippet:", body_text[:300])
            elif 'circular' in url.lower():
                print("Circular Page snippet:", body_text[:300])
            elif 'mandatory' in url.lower():
                print("Mandatory Disclosures snippet:", body_text[:300])
    except Exception as e:
        print(f"FAILED to fetch {url}: {e}")

