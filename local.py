#!/usr/bin/env python3
#def change():
#    a = 90
#    print(a)
#a = 9
#print("Before the function call ",a)
#print("inside change function",end = ' ')
#change()
#print("After the function call ",a)
a = 9
def change():
    global a
    print(a)
    a = 100
print("Before the function call ",a)
print("inside change function",end= ' ')
change()
print("After the function call ",a)
