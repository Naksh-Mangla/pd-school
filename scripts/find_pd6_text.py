with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('pd6.jpeg')
print(text[pos:pos+1500])

