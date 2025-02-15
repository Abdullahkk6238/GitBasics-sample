'''
# Dictionary and sets

info = {

    "name" : "affan",
    "subjects" : ["Python", "C", "Java"],
    "topics" : ("dict", "set"),
    "learning" : "coding",
    "age" : 30,
    "is_adult" : True,
    "marks" : 94.4,
    10.5 : 85.8
}
print(type(info))
print(info)

print(info["name"])

info["name"] = "Abdullah"
print(info["name"])

info["last_name"] = "kk"
print(info)

# Null / Empty dictionary

null_dict = {}

null_dict["name"] = "Aman"
print(null_dict)


# Nested Dictionary
student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)

print(student["subject"])


print(student["subject"]["chem"])



# Dictionary methods (Screenshot)

# Print all keys

student = {
    "name" : "rahul",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.keys())

print(list(student.keys()))

print(len(student))

print(student.values())

print(student.items())

pairs = list(student.items())

print(pairs[0])

print(student.get("name"))
print(student["name"])

# But if we give wrong 2nd will give error but first will give none

'''