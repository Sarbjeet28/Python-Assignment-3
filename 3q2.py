a = 10
def f():
 print ('Inside f() : ', a)
def g(): 
 a = 20
 print ('Inside g() : ',a)
def h(): 
 global a
 a = 30
 print ('Inside h() : ',a)
print ('global : ',a)
f()
print ('global : ',a)
g()
print ('global : ',a)
h()
print ('global : ',a)

output
============== RESTART: E:/python training/Assignment 3/3q2.py ==============
('global : ', 10)
('Inside f() : ', 10)
('global : ', 10)
('Inside g() : ', 20)
('global : ', 10)
('Inside h() : ', 30)
('global : ', 30)
>>> 
