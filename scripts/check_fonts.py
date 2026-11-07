with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

import re
fonts = re.findall(r'fonts\.googleapis\.com[^\'\"]+', html)
print('Google Fonts linked:', set(fonts))

socials = re.findall(r'href=[\"\'](https?://(?:www\.)?(?:facebook|instagram|twitter|youtube|linkedin)[^\"\']*)[\"\']', html, re.I)
print('Social URLs:', set(socials))

# Check for phone numbers
phones = re.findall(r'(?:\+?91[\s-]?)?[6-9]\d{9}', html)
print('Phone numbers:', set(phones))

# Check for emails
emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
print('Emails:', set(emails))

