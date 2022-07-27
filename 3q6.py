def outer():
 s="Ludhiana" 
 def inner1():
     s="punjab"
 def inner2():
     nonlocal s
     s="Chandigarh"
 def inner3():
     global s
     s="Haryana"
     
print(s) 
inner1() 
print(s) 
inner2()
print(s) 
inner3()
print(s)
outer()
print(s)

output
===================== RESTART: E:/python training/3q6.py =====================
Ludhiana
Chandigarh
Haryana   
Chandigarh
Haryana
