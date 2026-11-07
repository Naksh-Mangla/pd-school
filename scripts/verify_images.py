import urllib.request

test_images = [
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd9.png',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/Ch.-Kanwar-Pal-Gurjar-Education-Minister-Haryana-768x347.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/cooking-without-fire.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9781-1-768x512.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9784-300x200.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/MKS_9787-768x512.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220414-WA0002-1536x1156.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220112-WA0018-768x576.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20220820-WA0019-768x346.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0032-1-766x1024.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/IMG-20221101-WA0034-766x1024.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2019-03-25-at-09.40.29-1-1024x768.jpeg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd10-1024x780.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/1556209951_transportmainimage-768x512.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.54.56.jpeg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.00.jpeg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.02.jpeg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/WhatsApp-Image-2023-05-13-at-15.55.03.jpeg'
]

for url in test_images:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"OK ({r.status}) - {url.split('/')[-1]}")
    except Exception as e:
        print(f"FAILED - {url.split('/')[-1]}: {e}")

