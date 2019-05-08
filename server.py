import socket
import sys

# simple program to see what we receive on the port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
sock.bind(("127.0.0.1", 5005))

while True:
  data, addr = sock.recvfrom(2)
  
  print("received:", data)
  sys.stdout.flush() 