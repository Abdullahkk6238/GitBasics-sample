'''
lis = [1, 2, 3, 4, 5]
temp = lis[0]
lis[0] = lis[len(lis)-1]
lis[len(lis)-1] = temp
print(lis)


# Improved version

li = [1,5,6,8]
li[0], li[-1] = li[-1], li[0]
print(li)



li = [1,5,6,8]
li[0], li[3] = li[3], li[0]
print(li)

li = [1,5,6,8]

if 7 in li:
    print("Yes")
else:
    print("No")


li = [1,5,6,8]

li.reverse()
print(li)


licopy = li.copy()
print(licopy)

li = [1,5,6,8,5,6,4,5]

nc = int(input("Enter the number you want to get the count"))

if nc in li:
    print(li.count(nc))
else:
    print("Number not exist")
    
'''

