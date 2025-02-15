'''
class Student:
    name = "karan"
    
s1 = Student()
print(s1)

s2 = Student()
print(s2)

class Car:
    color = "Blue"
    brand = "mercedes"
    
    
car1 = Car()
print(car1.color)
print(car1.brand)


class Student:
    # Default constructors
    def __init__(self):
        pass

    # Parameterized constructors
    college_name = "ABC College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database...")

    
s1 = Student("karan", 97)
print(s1.name, s1.marks)

s2 = Student("arjun", 88)
print(s2.name, s2.marks)

print(s2.college_name)

print(Student.college_name)  // This also works

'''



        

    


