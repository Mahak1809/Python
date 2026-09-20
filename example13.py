student = {
    "name" : "Mahak",
    "age" : 20
}

print(student["name"])


student = {
    "name" : "Mahak",
    "age" : 20
}
student["age"] = 22
print(student["age"])
print(student)
student["city"] = "Indore"
print(student)
student.pop("age")
print(student.keys())
print(student.values())
print(student.items())
