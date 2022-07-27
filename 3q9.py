class Emp:
 def __init__(self,eid,ename,esal):
  self.eid=eid
  self.ename=ename
  self.esal=esal
 def __str__(self):
 		return "emp id=%d Emp name=%s Emp sal=%g"%(self.eid,self.ename,self.esal)
e1 = Emp(111,"kamal",100000.45)
print(e1)
e2 = Emp(111,"anu",200000.46)
print(e2)




class Test :
    @staticmethod
    def static_method_1():
        print('static method 1')

    @staticmethod
    def static_method_2() :
        Test.static_method_1()

    @classmethod
    def class_method_1(cls) :
        cls.static_method_2()

# call class method
Test.class_method_1()

output
============== RESTART: E:/python training/Assignment 3/3q9.py ==============
emp id=111 Emp name=kamal Emp sal=100000
emp id=111 Emp name=anu Emp sal=200000
static method 1
