'''
write a python code to do the following

i)  take input from user and search in google
ii)   pick the first 3 url of google search
iii)  make  QR-code of all 3 url's
iv)   Store all these qr-code in  apache web server in aws cloud
v)   share link of qrcode using aws public IP
'''

import pyqrcode
from googlesearch import search

n=input("Enter your search :")
url=[]
j=1
for i in search(n,stop=3):
	url.append(i)
	qr=pyqrcode.create(i)
	qr.svg(str(j)+".svg",scale=8)
	j=j+1

 
