#!/bin/Python3
import webbrowser
from googlesearch import search

f=open("urls.txt","w")
web = input("Enter topic to search : ")
x=search(web,stop=10)
for i in x:
	f.write(i+"\n")
webbrowser.open("https://www.google.com/search?q="+web)


