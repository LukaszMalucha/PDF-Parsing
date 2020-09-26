# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:31:48 2020

@author: LukaszMalucha
"""

f = open("text.txt", "a")
f.write("text file")
f.close()

pwd

f = open("text.txt", "r")
f.read()


f.seek(0)
f.read()

f.seek(0)
content = f.read()
print(content)
f.close()


f = open("text.txt", "r")
mylines = f.readlines()

for line in mylines:
    print(line[0])


myfile = open("text.txt", "w+")
myfile.close()

myfile = open("text2.txt", "a+")
myfile.write("test file line")
myfile.close()


with open("text.txt", 'r') as myfile:
    myvar = myfile.readlines()


