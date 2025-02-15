# Single line if / Ternary operator
'''
food = input("food: ")
eat = "Yes" if food == "cake" else "no"
print(eat)

# another method

food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


# Clever if / Ternanry operator

age = int(input("age: "))
vote = ("yes", "no") [age < 18]


# Type conversion
a = 2
b = 4.25

sum = a + b 
print(sum)

# Type casting
a = int("2")
b = 4.25

print(type(a))
sum = a + b 
print(sum)




# Practice problem 1

first = int(input("enter first number: "))
second = int(input("enter second number: "))

print("Sum =",first+second)


# Practice problem 2

side = int(input("Enter the length of the side"))
print("Area =",side * side)


first = float(input("enter first number: "))
second = float(input("enter second number: "))

print("Average =",(first + second)/2)



a = int(input("enter first number: "))
b = int(input("enter second number: "))

# if(a >= b):
#     print("True")
# else:
#     print("False")
    
print(a >= b)

'''

'''
# String Function

str = "apple"
print(str.endswith("ah"))

str = "apple"
print(str.capitalize())


str = "apple is a fruit"
print(str.replace("i","o"))
print(str.replace("is","are"))


str = "apple is a fruit"
print(str.find("i"))

str = "apple is a fruit"
print(str.count("i"))
'''

'''
# Practice Qn

# fname = input("Enter your first name: ")
# print("Length: ",len(fname))

str = "Apple $ is a $$ fruit"
print("Occurance of $: ",str.count("$"))




# Practice Qn

num = int(input("Enter the number"))

if(num%2==0):
    print(num, " is an even number")
else:
    print(num, " is an odd number")



num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if(num1 > num2 and num1 > num3):
    print(num1, "is greatest")
elif(num2 > num1 and num2 > num3):
    print(num2, "is greatest")
else:
    print(num3, "is greatest")
  
    
# Improved solution

num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))

if(num1 >= num2 and num1 >= num3):
    print(num1, "is largest")
elif(num2 > num3):
    print(num2, "is largest")
else:
    print(num3, "is largest")
'''

