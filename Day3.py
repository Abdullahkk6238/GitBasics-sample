'''
# Greatest among 4
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
num4 = int(input("Enter the fourth number"))

if(num1 >= num2 and num1 >= num3 and num1 > num4):
    print(num1, "is largest")
elif(num2 > num3 and num2 > num4):
    print(num2, "is largest")
elif(num3 > num4):
    print(num3, "is largest")
else:
    print(num4, "is largest")

# Multiple of 7 or not 
num = int(input("Enter a number"))

if(num%7==0):
    print(num, "is a multiple of 7")
else:
    print(num, "is not a multiple of 7")




# List and Tuple 
 
marks = [64.2, 87.2, 88.5, 97.5, 89.9]
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])

student = ["Affan",98.8, 17, "Delhi"]
print(student) 

### Strings and immutable and lists are mutable

str = "hello"
print(str[0])
str[0] = "a"  // not allowed


student = ["Affan",98.8, 17, "Delhi"]
print(student[0])
student[0] = "abdullah" 
print(student[0]) // allowed
# List slicing is also allowed


### List method

# look screenshot

list = [2,1,3,1]
list.append(4)
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.sort()
list1 = ['d', 'a', 'e']
list1.sort()
print(list1)

list1.reverse()
print(list1)

list1.insert(2,'b')
print(list1)

list.remove(1)
print(list)

list.pop(2)
print(list)


# Tupple

### List is mutable  and Tuple is immutable

tup = (1,5,7)
print(tup[0])
tupl()  -> valid
tupl(1,)  -> if single => , should be there

tup.index(5)
tup.count(1)


# Practice Problem 

f1 = input("Enter first fruit:")
f2 = input("Enter Second  fruit: ")
f3 = input("Enter third fruit: ")

list = [f1, f2, f3]

print(list)

# Improved version

fruits = []
fruits.append(input("Enter the 1st fruit"))
fruits.append(input("Enter the 2nd fruit"))
fruits.append(input("Enter the third fruit"))

print(list)


# Practice problem

list1 = [1, 2, 4, 2, 1]
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("Palindrome")
else:
    print("NOT Palindrome")


# Practice Problem

tup = ("C","D", "A", "A", "B", "B", "A")

print(tup.count("A"))
    
lis = ["C","D", "A", "A", "B", "B", "A"]
lis.sort()
print(lis)
'''



