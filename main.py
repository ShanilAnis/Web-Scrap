# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode())
#
# mysock.close()



import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0)+ 1
# print(counts)

ehand = urllib.request.urlopen('https://www.dr-chuck.com/page1.html')
# for line in ehand:
    # print(line.decode().split())
    # print(line.decode().strip())

from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname =False
ctx.load_verify_mode = ssl.CERT_NONE

url = input("Enter >-")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags =soup.find('a', {'class': 'item-title'}).text
print(tags.strip())
