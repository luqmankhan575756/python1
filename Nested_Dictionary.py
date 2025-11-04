student = {
    "name" : "abdullah",
    "subjects" : {
        "phy" : 97,
        "chem" : 98,
        "phys" : 94
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])
# this is called Nested Dictionary

print(student.keys())  #my_dicationary.keys
print(student.__len__())  
print(student.values())
print(student.items())
print(student["name"])
print(student.get("name"))
new_dict = { "city" : "delhi"}
student.update(new_dict)
print(student)