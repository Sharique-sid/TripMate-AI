import urllib.request
import re

url = 'https://magicdecor.in/wallpaper/travel/?srsltid=AfmBOoorlV18rlymtaAJqmWIosz1TzCNmZWW8kRwOjEfflHYrgI1SqsZ'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'<img[^>]+src=["\']([^"\']+)["\']', html)
    
    valid = []
    for m in matches:
        if ('jpg' in m or 'png' in m or 'webp' in m or 'jpeg' in m):
            valid.append(m)
    
    print("MATCHES:")
    for m in valid[:20]:
        print(m)
except Exception as e:
    print(e)
