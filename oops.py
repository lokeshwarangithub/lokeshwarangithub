#class and objects.....
"""
class Goa():
    name=""
    drink=""
    def party(self):
        print("lets party")

    def beach(self):
        print("Enjoy the beach")


ramesh = Goa()
suresh = Goa()


ramesh.name="Ramesh"
ramesh.age ="22"
suresh.name="Suresh"
suresh.age ="34"
ramesh.drink="yes"
suresh.drink="no"

print(ramesh.name)
print(ramesh.age)

print(suresh.name)

print(suresh.age)
print("drink:", ramesh.drink)
print("drink:", suresh.drink)
"""
"""
class Laptop():
    price=0
    ram=""
    proc=""
    def __init__(self):#class constuctor
        self.price=0
        self.ram=""
        self.proc=""
        
    def display(self):
        print("price:",self.price)
        print("ram:",self.ram)
        print("proc:",self.proc)

        
hp=Laptop()
hp.price=50000
hp.ram="8gb"
hp.proc="i5"


dell=Laptop()
dell.price=60000
dell.proc="i7"
dell.ram="16gb"


dell.display()
hp.display()
"""


"""
class Student():
    def __init__(self):
        self.name ="oweinf"
        self.regno ="2342"

    def display(self):
        print("name",self.name)
        print("regno",self.regno)
s1=Student()
s2=Student()

s1.name="manoj"
s1.regno="1"

s2.name="loki"
s2.regno="2"

s1.display()
s2.display()
"""




"""
class fruit():
    def __init__(self):
        self.color ="color"
        self.name ="red"

    def display(self):
        print("color",self.color)
        print("name",self.name)


a1=fruit()
a1.color="redcolor"
a1.name="red"

a1.display()

class teacher():
    def __init__(self,name,regno):#class constructor
        self.name=name
        self.regno=regno

    def display(self):
        print("Name: ",self.name)
        print("Regno:",self.regno)



t1=teacher("prem","1")
t2=teacher("venky","2")

t1.display()
t2.display()
"""
"""

class calculator():
    def add(self,a,b):
        print("add",a+b)


obj=calculator()
obj.add(12,13)

"""
"""

#class variables

class phone():
    chargertyp="c-type"#class variable
    def __init__(self,brand,price):
        self.brand=brand#instance variable
        self.price=price

        
    def display(self):
        print("Brand: ",self.brand)
        print("price: ",self.price)
        print("chargertyp: ",self.chargertyp)
        
        
phone.chargertyp="b-typ"

oppo=phone("oppo F21","24000")
oppo.display()


redmi=phone("mi","12000",)
redmi.display()


moto=phone("moto21","12000")
moto.display()
"""
"""
#in python function is called as methods in oops on python

class laptop():
    chargertyp="c-typ"   #class variable


    def __init__(self):
        self.brand=""    #intance variable
        self.price=34

    def setprice(self,price):#instance method
        self.price=price

    def getprice(self):
        print(self.price)

        
    @classmethod   #class method
    def changchargertyp(cls):
        cls.chargertyp="B-type"
        print("charger type changed to b")
        
    @staticmethod
    def info():
        print("this is laptop class")
        


hp=laptop()
hp.setprice(40000)
hp.getprice()



laptop.changchargertyp()
hp.info()




#inheritance
#(!)
class dad():
    def phone(self):
        print("dads phone")

class mom():
    def sweet(self):
        print("moms sweet")

class son1():
    def laptop(self):
        print("sons laptop")

class son2(son1):
    def tab(self):
        print("son2 tab")



dev=son2()
dev.tab()
dev.laptop()

"""

"""
#multilevel inheritance
class grandpa():
    def phone(self):
        print("grandpa phone")

class dad(grandpa):
    def money(self):
        print("dads money")

class son(dad):
    def laptop(self):
        print("laptop owned")



venky=son()
venky.laptop()
venky.money()
venky.phone()

"""
"""
#hirarical inheritance&hybrid inheritance
class dad():
    def money(self):
        print("money want")
        
class land():
    def importland():
        print("asal own")


class son1(dad,land):
    pass

class son2(dad):
    pass

class son3(dad):
    pass



s1=son1()
s1.money()

"""
"""
#superkeyword
class a():
    def __init__(self):
        print("rcb never won cup")

        
    def display(self):
        print("you are in class a")


class b():
    def __init__(self):
        super().__init__()
        print("CSK won 5 cup")

        
    def display(self):
        print("you are in class b")


class c(b,a):
    def __init__(self):
        super().__init__()
        print("MI won 5 cup")

    def display(self):
        print("you are in class c")




obj1=c()
"""
"""
#polymorphism
#one to many

def add(a,b,c=0,d=0):
    print(a+b+c+d)

add(1,2)
add(1,2,3)
add(1,2,3,4)
"""
"""
class Animal():#method overriding
    def sound(self):
        print("animal make sound")

        

class Dog(Animal):
    def sound(self):
        print("Dog barks")

        
class Bird(Animal):
    def sound(self):
        print("Bird sing")
        
        

b1=Bird()
b1.sound()

"""


"""
class shape():
    def area(self):
        return 0

class rectangle(shape):
    def area(self):
        l = 10
        b = 20
        print(l*b)


        

r1=rectangle()
r1.area()

"""

"""
class person():
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):#super keyword
        super().__init__(name)
        self.grade=grade
        
      
    def display(self):
        print(self.name,self.grade)






s1=student("loki","A")
s1.display()
"""

"""
class Employee():
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self,depaertment):
        super().__init__(name, salary)
        self.department=department

    def display(self):
        print(self.name,self.salary,self.department)


m1=Manager("loki","12000","CSE")
m1.display()
"""

"""

#Encapsulation

class Company():
    def __init__(self):
        self._companyName="Google" #__private variable  

class b(Company):                  #_protected variable
    pass

        

b1 = b()
print(b1._companyName)

"""

"""
class Car():
    def accelerate(self,name):
        print("hello{raja},lets drive")

my_car=Car()
my_car.accelerate("raja")


class dog():
    def __init__(self,name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print("Bark")

    def getInfo(self):
        return {name: self.name,
                age: self.age,
                breed: self.breed}

a1=dog()
a1.bark()
a1.getInfo("tim",4,"beagle")

"""



class Dog:
    def bark(self):
        print("boww boww")

d = Dog()
print(type(d))
d.bark()


    
