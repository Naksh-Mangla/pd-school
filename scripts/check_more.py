import urllib.request
import re

def check_detail(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=10)
    html = resp.read().decode('utf-8', errors='ignore')
    return html

# Check Video Gallery
vg_html = check_detail('https://pdpublicschool.co.in/video-gallery/')
iframes = re.findall(r'<iframe[^>]+src=["\'](.*?)["\']', vg_html, re.I)
print("Video Gallery iframes / embeds:", iframes)

# Check Circular
circ_html = check_detail('https://pdpublicschool.co.in/circular/')
pdf_links = re.findall(r'href=["\']([^"\']+\.pdf)["\']', circ_html, re.I)
print("Circular PDFs:", pdf_links)
# Clean text in circular
clean_c = re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>', '', circ_html, flags=re.DOTALL | re.I)
text_c = re.sub(r'<[^>]+>', ' ', clean_c)
print("Circular text:", ' '.join(text_c.split())[:400])

# Check Contact Us
contact_html = check_detail('https://pdpublicschool.co.in/contact-us/')
clean_ct = re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>', '', contact_html, flags=re.DOTALL | re.I)
print("Contact text:", ' '.join(re.sub(r'<[^>]+>', ' ', clean_ct).split())[:400])

