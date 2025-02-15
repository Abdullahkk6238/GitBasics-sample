'''
# Guess the number 

import random

target = random.randint(1, 100)

while True:
    userChoice = input("Guess the target Or Quit(Q) : ")
    if(userChoice == "Q"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success : Correct Guess!!")
        break 
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")
    

print("-----Game Over-----")

'''
# Random Password generator

import random
import string


# print(string.ascii_letters)
# val = random.choice([1, 2, 3])
# print(val)

pass_len = 8
charValues = string.ascii_letters + string.digits + string.punctuation


#List comprehension [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])


# password = ""
# for i in range(pass_len):
#     password += (random.choice(charValues))


print("Your random password is :", password)


 