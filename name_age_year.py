#!/bin/python3
import datetime
name=input("Your Name : ")
age=int(input("Your Age : "))
d=datetime.datetime.now()

print("{} you will turn 95 by the year : {}".format(name,(95-age)+d.year))

