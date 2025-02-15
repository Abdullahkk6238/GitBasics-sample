'''
def oddOrEven(n):
    if(n%2 == 0):
        return "EVEN"
    else:
        return "ODD"
n = 6

res = oddOrEven(n)
print(res)


# Recursive Function  (Call Stack)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(5)


def fact(n):
    if(n == 0 or n ==1):
        return 1
    return n * fact(n-1)


print(fact(5))


def sumOfN(n):
    if(n == 1):
        return 1
    return n + sumOfN(n-1)

sum = sumOfN(5)
print(sum)


def pri_list(list, index):
    if(index == len(list)):
        return
    print(list[index])
    pri_list(list,index+1)
    
list = [1, 2, 3, 4, 5]

pri_list(list, 0)


# File I/O

f = open("Day7demo.txt", "r")
data = f.read()
print(data)

f.close()

f = open("Day7demo.txt", "r")
data = f.read(5)
print(data)

f.close()

f = open("Day7demo.txt", "r")


line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

f.close()


# Writing to a file (w,a)

f = open("Day7demo.txt", "w")
f.write("I want to learn javascript tomorrow. 123")

f.close()


f = open("Day7demo.txt", "a")
f.write(" Then i will move to ReactJS")

f.close()


f = open("Day7demo.txt", "a")
f.write(" \nAfter that nodeJS")

f.close()

# Look stackflow for different modes
# Important screenshot 
# With syntax
# to install a module write pip or pip3 install module_name

# Deleting a file

import os
os.remove("sample.txt")


# Practice Qn 

f = open("practice.txt","w+")

f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")

f.close()


# Improved version

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")    


with open("practice.txt","r") as f:
    data = f.read()
    
new_data = data.replace("Java", "Python")
print(new_data)
        
with open("practice.txt","w") as f:
    f.write(new_data)


def check_for_word():
    word = "learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(data.find(word) != -1):
            print("FOUND")
        else:
            print("NOT FOUND")
         

check_for_word()
 
            
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt") as f:
        while data:
            data = f.readline()
            if(word in data):
                return line_no
            line_no += 1
    return -1

print(check_for_line())
 
                
               
with open("practice.txt", "r") as f:
    data = f.read()
    
    
    num = ""
    
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
 
count = 0   
with open("practice.txt", "r") as f:
    data = f.read()
    
    nums = data.split(",")
    for i in nums:
        if(int(i) % 2 == 0):
            count += 1
print(count)

'''