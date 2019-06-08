import os
import shutil

if not os.path.exists("/temporary"):
	os.mkdir("/temporary")
else:
	shutil.rmtree("/temporary")
	os.mkdir("/temporary")	
for i in range(200):
	name="New_folder"+str(i)
	file="New_file"	+ str(i)+".txt"
	os.mkdir("/temporary/"+name)

for i in range(100):
	file="New_file"	+ str(i)+".txt"
	os.mknod("/temporary/"+file)
