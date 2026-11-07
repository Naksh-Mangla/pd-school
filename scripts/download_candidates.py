import urllib.request
import os

images_to_check = {
    'about_school': 'https://pdpublicschool.co.in/wp-content/uploads/2024/05/about-school.jpg',
    'pd6': 'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd6.jpeg',
    'img_3032': 'https://pdpublicschool.co.in/wp-content/uploads/2025/04/IMG_3032-scaled.jpg',
    'img_2997': 'https://pdpublicschool.co.in/wp-content/uploads/2025/04/IMG_2997-scaled.jpg',
    'dsc_9009': 'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_9009-scaled.jpg',
    'dsc_7609': 'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_7609.jpg',
    'whatsapp_2025': 'https://pdpublicschool.co.in/wp-content/uploads/2025/12/WhatsApp-Image-2025-12-19-at-09.46.22.jpeg'
}

for name, url in images_to_check.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = r.read()
            filename = f"{name}.jpg"
            with open(filename, 'wb') as f:
                f.write(data)
            print(f"Downloaded {filename}: {len(data)} bytes")
    except Exception as e:
        print(f"Error {name}: {e}")

