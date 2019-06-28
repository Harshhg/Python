#!/usr/bin/python3
import cgi
import subprocess
import cgitb
# To show common errors in webbrowser
cgitb.enable()   # CGI Traceback... display errors in browser..
print("Content-type:text/html")
print("")


webdata=cgi.FieldStorage()    # This will collect all the HTML code with data.
# Now extracting value of X
first_name=webdata.getvalue('fn')  # Gets the value of the First Name from FORM
command=webdata.getvalue('cmd')   # Gets the command user enters from FORM

# Using subprocess to integrate with linux.
result=subprocess.getoutput(command)   # Execute the command in linux and store output in variable.

# Sending output of client via web browser
print("<pre>")
print(first_name+" your output is: "+result)
print("</pre>")
