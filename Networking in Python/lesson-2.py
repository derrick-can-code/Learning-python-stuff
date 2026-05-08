#instead of importing sockets, and encoding and decoding, the library urllib provides a faster way to do this
import urllib.request, urllib.parse, urllib.error

#this basically does everything, from encoding file in UTF-8, then opening in the web socket
#now, we have access to file and can do anything to it
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

for line in fhand:
  #we first decode it
  #print(line.decode())
  #when it comes, it comes with white spaces, so we strip them off
  print(line.decode().strip())
  
  
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
  words = line.decode().split()
  
  for word in words:
    counts[word] = counts.get(word, 0) + 1
    
print(counts)
  