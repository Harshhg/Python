import cgi,subprocess
import cgi
import cgitb
import os
import time
import webbrowser

cgitb.enable()
print("Content-type:text/html")
print("")


web=cgi.FieldStorage()
data=web.getvalue('install')

print("Jupyter is installing and running")
subprocess.getoutput('sudo pip3 install jupyter')

os.system("jupyter-notebook --ip=0.0.0.0 --port=8888 &>/dev/null &")
time.sleep(5)
x=subprocess.getoutput("jupyter-notebook list | sed 1d | awk '{print $1}' | awk -F[?:] '{print $4}'")
url="http://13.233.108.214:8888/?"+x
print('''
<html>
<head>
<script type="text/javascript">
function load()
{
window.open(%s,'_blank');
}
</script>
</head>
<body onload="load()">
</body>
</html>
''' %url)
