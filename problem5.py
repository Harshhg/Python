#!/bin/python3
# 0.00 - 12.00 --> Good Morning
# 12.00 - 17.00 --> Good Afternoon
# 17.00 - 21.00 --> Good Evening
# 21.00 - 0.00 --> Good Night
import datetime

name =input("Enter your Name : ")
d=datetime.datetime.now()
curhour=d.hour
curmin=d.minute
if curhour<12:
	print("Good Morning",name+"!")
elif curhour>11 and curhour<=16:
	print("Good Afternoon",name+"!")
elif curhour > 16 and curhour <=21:
	print("Good Evening",name+"!")
else:
	print("Good Night", name+"!")
