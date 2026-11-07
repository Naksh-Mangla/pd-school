with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re
tags = ['html', 'head', 'body', 'header', 'main', 'footer', 'script']
for t in tags:
    open_c = len(re.findall(r'<' + t + r'[\s>]', content, re.I))
    close_c = len(re.findall(r'</' + t + r'>', content, re.I))
    print(f'Tag <{t}>: open={open_c}, close={close_c}')

links = re.findall(r'href=["\'](#[^"\']+)["\']', content)
print('Anchor links:', set(links))
for a in set(links):
    target = a[1:]
    found = f'id="{target}"' in content or f"id='{target}'" in content
    print(f'Anchor {a} target exists:', found)

