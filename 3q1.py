def a_fun():
 global name
 name = 'A'
def b_fun():
 global name
 name = 'B'
b_fun()
a_fun()
print (name)

output
============== RESTART: E:/python training/Assignment 3/3q1.py ==============
A
