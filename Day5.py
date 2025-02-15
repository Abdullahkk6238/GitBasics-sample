'''
student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

student.update({"city" : "delhi", "age" : 16})

# new_dic = {"city" : "delhi"} // This also works
# student.update(new_dic)     //

print(student)
'''
'''
# Set // ignore duplicate , unordered // Set is mutable but the element in the set is immutable // Thats why we cannot inset list and dic

collection = {1, 2, 2, 3,  3, 4, "hello", "world"}

print(collection)
print(type(collection))
print(len(collection))


collection = set()

collection.add(1)

collection.add(2)
collection.add(3)
print(collection)

collection.remove(1)

print(collection)

collection.clear()

print(len(collection))


collection.add(2)
collection.add(3)

print(collection.pop()) // Remove random number



# Union and intersection

set1 = {1, 2, 3}

set2 = {2, 3, 4}

print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))


dict = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : "a small animal"
}

print(dict)


sub = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}

print("The number of classroom needed : ",len(sub))


marks = {}
maths = int(input("enter the marks of maths"))
phy = int(input("enter the marks of phy"))
che = int(input("enter the marks of che"))

marks.update({
    "maths" : maths,
    "phy" : phy,
    "che" : che
})


print(marks)



set = {9, "9.0"}

print(set)


set = {
    ("float", 9.0),
    ("int", 9)
}

print(set)


# Loops 

# while loop

count = 1 

while count <= 5:
    print("hello")
    count += 1

print(count)    

i = 1    // Iterator
while i <= 5:
    print("hello")
    i += 1


# 
 
i = 1

while i <= 100:
    print(i)
    i += 1


i = 100

while i >= 1:
    print(i)
    i -= 1


n = int(input("Enter the number"))

i = 1
while i <= 10:
    print(n, " * ", i ," = ",n*i )
    i += 1
    



list = [1, 4, 9, 25, 36, 49, 64, 81, 100]
i = 0
while i < len(list):
    print(list[i])
    i += 1
    

tup = (1, 4, 9, 25, 36, 49, 64, 81, 100)

x = int(input("enter the number"))
flag = 0
i = 0
while i < len(tup):
    if(x == tup[i]):
        flag = 1
        break
    i += 1
if(flag == 0):
    print(x, " not found")
else:
    print(x, " found at position ", i+1)


# Improved version 
tup = (1, 4, 9, 25, 36, 49, 64, 81, 100)

x = int(input("enter the number"))

i = 0

while i < len(tup):
    if(tup[i] == x):
        print("FOUND at index", i)
        break
    i += 1


str = "Abdullah"
for i in str:
    print(i)
else:    # This will use in case of break
    print("END")    



lis = [1, 4, 9, 25, 36, 49, 64, 81, 100]

for i in lis:
    print(i)


tup = (1, 4, 9, 25, 36, 49, 64, 81, 100)
x = int(input("Enter the number"))
idx = 0
for i in tup:
    if(i == x):
        print(x, "found at index",idx)
        break
    idx += 1
'''



    

