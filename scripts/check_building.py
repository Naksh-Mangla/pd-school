import urllib.request

urls = [
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/about-school.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2024/05/pd6.jpeg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_8249-scaled.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_9009-scaled.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/04/IMG_3032-scaled.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/04/IMG_2997-scaled.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_8204.jpg',
    'https://pdpublicschool.co.in/wp-content/uploads/2025/03/DSC_7609.jpg'
]

for u in urls:
    try:
        req = urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'}, method='HEAD')
        with urllib.request.urlopen(req, timeout=5) as r:
            print(f"STATUS: {r.status}, LEN: {r.headers.get('Content-Length')}, URL: {u.split('/')[-1]}")
    except Exception as e:
        print(f"ERR: {e}, URL: {u.split('/')[-1]}")

