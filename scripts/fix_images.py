with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace pd4 with the real building photo pd6.jpeg
text = text.replace(
    'https://pdpublicschool.co.in/wp-content/uploads/2024/04/pd4-1024x768.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd6.jpeg'
)

# Replace pd10 with the real sports track photo MKS_9781-1-768x512.jpg
text = text.replace(
    '<!-- Campus Grounds & Play Area (pd10-1024x780.jpg) -->',
    '<!-- Campus Sports & Play Area (MKS_9781-1-768x512.jpg) -->'
)
text = text.replace(
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd10-1024x780.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9781-1-768x512.jpg'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Success!')

