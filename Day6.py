'''
# Range function range(start?, stop, step?)

for i in range(10):
    print(i)
    
    
for i in range(2, 10):
    print(i)

for i in range(2, 10, 2):
    print(i)


# Practice Qn 

for i in range(1,101):
    print(i)


for i in range(100,0,-1):
    print(i)


n = int(input("enter the number: "))
for i in range(1,11):
    print(n*i)
    
# Pass



sum = 0
    
i = 1
while i <=n:
    sum   += i
    i += 1
print("Sum : ",sum)


n = int(int(input("enter the number")))
fact =1
for i in range(1,n+1):
    fact *= i
print("Factorial : ",fact)



# Function 

def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum

calc_sum(5, 10)

calc_sum(2, 10)

calc_sum(12, 17)

# Improved

def calc_sum(a, b):
    return a + b

sum = calc_sum(1, 2)
print(sum)


def avg(a, b, c):
    average = (a+b+c)/3
    print("Average : ",average)
    
a = 10
b = 4
c = 7
avg(a,b,c)


print("apnacollege", end=" ") # End is a parameter , default \n
print("Abdullah") 

def cal_produ(a=1, b=1):  #default // if one is default is must be in last
    print(a * b)

cal_produ()


# Practice problems



num = [1, 5, 6, 8, 10]
name = ["Abdullah", "Affan", "Aarif"]

def len_list(list):
    print(len(list))

len_list(num)
len_list(name)


name = ["Abdullah", "Affan", "Aarif"]

def pri_list(list):
    for i in list:
        print(i,end=" ")
    
pri_list(name)



def calc_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("Factorial : ",fact)
n = int(input("Enter the num"))

calc_fact(n) 


def usd_inr(n):
    print(n ,"USD =",n *83, "INR")
    
n = int(input("Enter the USD : "))
usd_inr(n) 
'''


