a,b,x,y = 1,15,3,4
def fun(x, y):
 global a
 a = 42
 x,y = y,x
 b = 33
 b = 17
 c = 100
print (a,b,x,y)
fun(17,4)
print (a,b,x,y)

output
============== RESTART: E:/python training/Assignment 3/3q4.py ==============
(1, 15, 3, 4)
(42, 15, 3, 4)
