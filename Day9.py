'''
# Class Methods

class Student:
    college_name = "ABC College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def welcome(self):
        print("welcome student,", self.name)
    
    def get_marks(self):
        return self.marks
        
        
s1 = Student("karan", 97)
s1.welcome()
print(s1.get_marks())


# Practice Qn

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod
    def hello():
        print("hello")
        
    def calc_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi",self.name,"Average = ",sum/3)
        
s1 = Student("karan", [98, 97, 88])
s1.calc_avg()
s1.hello()

s1.name = "ironman"
s1.calc_avg()


# Abstraction 
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch  = False
    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")
        
        
car1 = Car()

car1.start()


class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no
    
    # Debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"was debited")
        print("total balance : ",self.get_balancee())
        
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance : ",self.get_balancee())
        
    def get_balancee(self):
        return self.balance
    
    
        
acc1 = Account(10000, 12345)
acc1.debit(1000)

acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)

# Del keyword

class Student:
    def __init__(self, name, ):
        self.name = name
        
s1 = Student("shradha")
print(s1.name)
del s1.name
print(s1.name)



class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345", "abcde")

print(acc1.acc_no)
print(acc1.reset_pass())



class Person:
    __name = "anonymous"
    
    
    def __hello(self):
        print("hello Person!...")
        
        
    def welcome(self):
        self.__hello()
        
    


p1 = Person()

print(p1.welcome())


# Inheritance

class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
        
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.name)
print(car1.start())



class Car:
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand
        
        
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
        
        
        
car1 = Fortuner("diesel")
car1.start()


# Multiple Inheritance

class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to class B"
    
class C(A, B):
    varC = "welcome to class C"
    
    
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)


class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car started...")
    
    @staticmethod
    def stop():
        print("Car stopped...")
        
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = ToyotaCar("prius", "electric")

print(car1.type)



class Person:
    name = "anonymous"
    
    # def changeName(self, name):
    #     # Person.name = name (Same as below)
    #     self.__class__.name = "Rahul"
        
    @classmethod
    def changeName(cls, name):
        cls.name = name
        
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        self.percentage = str((self.phy + self.chem + self.math) / 3) +"%"
        
    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math) / 3) +"%"
        
        
stud1 = Student(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86
print(stud1.phy)
stud1.calcPercentage()
print(stud1.percentage)

# property


class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) +"%"
        
        
stud1 = Student(98, 97, 99)
print(stud1.percentage)

stud1.phy = 86

print(stud1.percentage)


# Polymorphism

print(1 + 2) #3 
print("apnap" + "college") #concatenate
print([1, 2, 3, 4] + [5, 6, 7]) #merge

# 
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def ShowNumber(self):
        print(self.real, "i +", self.img, "j")
        
    def add(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
        
num1 = Complex(1, 3)
num1.ShowNumber()

num2 = Complex(4, 6)
num2.ShowNumber()

num3 = num1.add(num2)
num3.ShowNumber() 

# Dunder functions (__add__) (same above with dunder functions)


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def ShowNumber(self):
        print(self.real, "i +", self.img, "j")
        
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
        
        
num1 = Complex(1, 3)
num1.ShowNumber()

num2 = Complex(4, 6)
num2.ShowNumber()

num3 = num1 + num2
num3.ShowNumber() 

num4 = num1 - num2
num4.ShowNumber()


class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def Area(self):
        return (22/7) * self.radius ** 2
    
    
    def Peri(self):
        return 2 * (22/7) * self.radius
    
c1 = Circle(21)
print(c1.Area())

print(c1.Peri())   


class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print("role =",self.role)
        print("Department = ",self.department)
        print("Salary = ", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")
        
        
engg1 = Engineer("Elon Musk", 40)
engg1.showDetails()
'''

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    
    def __gt__(self, ord2):
        return self.price > ord2.price
        
    
    
ord1 = Order("chips", 20)
ord2 = Order("tea", 15)

print(ord1 > ord2)

    