#a web socket allows constant coversation between a client and a server
#unline traditional HTTP where client has to refresh a page for data anytime, 
#websocket keeps a singgle connection open

#building a web socket in python is easy, and requires only three lines of code
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
  data = mysock.recv(512)
  if len(data) < 1:
    break
  print(data.decode())
  
mysock.close()
