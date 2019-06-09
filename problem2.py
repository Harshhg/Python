#!/bin/Python3
import webbrowser
from googlesearch import search
web = input("Enter topic to search : ")
x=search(web,stop=10)
res=[]
for i in x:
        res.append(i)
webbrowser.open("https://www.google.com/search?q="+web)
print(res)

