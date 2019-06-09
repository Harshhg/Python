#!/bin/python3

adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
x=[]
y=[]
print("1. Numbers greater than 5 :")
for i in adhoc:
	if i>5:
		print(i)
		x.append(i)
print("2. Numbers less than or equal to 2 : ")
for i in adhoc :
	if i <=2 :
		print(i)
		y.append(i)

print("List 1 is :",x)
print("List 2 is :",y)


