##class My_Class:
##    def fun():
##        print("hello")
##        
##My_Class.fun()
#unbounded class (class without constructor)

##class My_Class:
##    my_data = "dhoni"
##    
##    def fun():
##        print("hello")
##        
##My_Class.fun()
##print(My_Class.my_data)

##class My_Class:
##    my_data = "dhoni"
##    
##    def fun():
##        print("hello")
##
##my = My_Class 
##my.fun()
##print(my.my_data)

##class My_Server:
##
##    def Hostname(ip):
##
##        print(ip)
##
##    def Login(ip,pwd):
##
##         print(ip,pwd)
##
##my = My_Server
##my.Hostname("2.2.2.2")
##my.Login("2.2.2.2","123")
##
##class My_Server:
##    
##    def __init__(punith,ip,pwd):
##
##        punith.a = ip
##        punith.b = pwd
##        
##
##    def Hostname(self):
##
##        print(self.a)
##
##    def Login(self):
##
##         print(self.a, self.b)
##
##my = My_Server("2.2.2.2","123") #Constructor is formed #my - instance object (Single Memory)
##my.Hostname()
##my.Login()
#whenever you create a constructor it will create a empty space for internal reference


##class My_Server:
##    
##    """Class My_Server is defined with two fuction
##       __author__ : Mohan
##       __data__ :  """
##    def Hostname(self):
##
##        print("hello")
##
##    def Login(self):
##
##         print("welcome")
##
##my = My_Server() #Constructor is formed #my - instance object (Single Memory)
##my.Hostname()
##my.Login()
##print(my.__doc__)

##class My_Server:
##    __my_data = "dhoni"
##  
##    def Hostname(self):
##
##        print("hello")
##
##    def __Login(self):
##
##         print("welcome")
##
##my = My_Server() 
##my.Hostname()
##my.Login()
##print(my.my_data)

#oops - access specifier private public

##class My_Server:
##   
##  
##    def Hostname(self):
##
##        print("hello")
##
##    def Hostname(self):
##
##         print("welcome")
##
##my = My_Server() 
##my.Hostname()


##class My_Server:
##   
##  
##    def Hostname(self):
##
##        print("hello")
##
##    def __Hostname(self):
##
##         print("welcome")
##
##my = My_Server() 
##my.Hostname()

##class My_Server:
##
##    def __init__(self,ip,pwd):
##
##        self.a = ip
##        self.b = pwd
##  
##    def Hostname(self):
##
##        print(self.a)
##        
##class My_Server2(My_Server):
##    
##    def __init__(self,ip,pwd):
##
##        self.d = ip
##        self.e = pwd
##
##    def Hostname2(self):
##
##         print(self.d, self.e)
##
##my = My_Server2("2.2.2.2",123) 
##my.Hostname()
##my.Hostname2()

class A:

    def fun(self):
        print("A")
class B(A):

    def fun(self):
        print("B")
class C(A):

    def fun(self):
        print("C")

class D(C,B):
    pass

#MRO method resolution order
    
d = D()
d.fun()






































































































