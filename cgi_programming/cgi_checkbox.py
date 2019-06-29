#!/usr/bin/python3

import cgi
import cgitb
import subprocess

cgitb.enable()
print("Content-type:text/html")
print("")



print("""

<html>
<h1> CGI scripting </h1>
<body bgcolor="linen">
<form method="post" action="cgi_checkbox.py">

Enter Your name : <input type="text" name="name"><br>
Select command: <br>
<input type="checkbox" name="ls" value="ls"> ls - "For listing directory" <br>
<input type="checkbox" name="date" value="date"> date - "For Current Date" <br>
<input type="checkbox" name="cal" value="cal"> cal - "For calender"<br>
<input type="checkbox" name="fdisk" value="sudo fdisk -l" > fdisk -l " For Disk partitions"<br><br>
<input type="submit" value="Submit">
</form>
</body>
</html>

""")
cmd=""
form=cgi.FieldStorage()
if form.getvalue("ls"):
	cmd=form.getvalue("ls")
if form.getvalue("date"):
	cmd=form.getvalue("date")
if form.getvalue("cal"):
	cmd=form.getvalue("cal")
if form.getvalue("fdisk"):
	cmd=form.getvalue("fdisk")
result=subprocess.getoutput(cmd)
print("<pre>%s</pre>" %result)




