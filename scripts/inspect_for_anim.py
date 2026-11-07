import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's inspect CSS styles and script blocks
print("Length of index.html:", len(html))

