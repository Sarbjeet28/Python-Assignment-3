def f():
 x = 42
 def g():
  global x
  x = 43
 print("Before calling g: ",x)
 g()
 print("After calling g: ",x)
 
f()
print("x in main: " ,x)

output
===================== RESTART: E:/python training/3q5.py =====================
('Before calling g: ', 42)
('After calling g: ', 42)
('x in main: ', 43)
