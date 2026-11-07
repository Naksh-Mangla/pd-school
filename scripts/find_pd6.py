with open('homepage.html', 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

pos = text.find('pd6.jpeg')
if pos != -1:
    print("=== CONTEXT OF pd6.jpeg ===")
    print(text[max(0, pos-400):min(len(text), pos+400)])
else:
    print("pd6.jpeg not found")

