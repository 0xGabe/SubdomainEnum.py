import socket
import sys

domain = sys.argv[1]

with open(sys.argv[2]) as file:
    lines = file.readlines()
for i in lines:
    DNS = i.strip("\n") + "." + domain
    try:
        print(DNS +": "+ socket.gethostbyname(DNS))
    except socket.gaierror:
        pass
