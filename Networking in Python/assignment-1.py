#sample work
#import libraries required, url lib and beautiful soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignoring the ssl errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter url - ")
count = int(input("Enter count - "))
position = int(input("Enter position - "))

for i in range(count):
  #open current url
  html = urllib.request.urlopen(url, context= ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  
  #retrieve all anchor tags
  tags = soup('a')
  
  #find link at a specific position
  target_tag = tags[position - 1]
  
  #update the url for next iteration
  url = target_tag.get('href', None)
  name = target_tag.contents[0]
  
  print(f"Retrieving: {url}")
  
print(f"\nThe last name in the sequence is: {name}")    