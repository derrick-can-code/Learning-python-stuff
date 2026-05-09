import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignoring the ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
html = urllib.request.urlopen(url, context= ctx).read()
soup = BeautifulSoup(html, 'html.parser')

sum = 0

#retrieving span anchor tags
tags = soup('span')
length = len(tags)

for tag in tags:
  num = int(tag.contents[0])
  sum += num

print(f"Count {length}")
print(f"Sum {sum}")