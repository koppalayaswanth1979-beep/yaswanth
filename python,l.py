#dictionaries in python
student={
    "name":"bhanu",
    "age":18,
    "course":"python"}
print(student)


#change values in a dictionary
student["age"]=18
print(student["age"])

#add new data to a dictionary
student["city"]="vijayawada"
print(student)
...


#remove data
student.pop("city")
print(student)

student={
	"name": "chandra sekhar",
	"age": 21,
	"course": "python"
}
print(student.items())
print(student.get("name"))
student.update({"age": 18})
print(student)
student.pop("age")
print(student)

pop item
student ={
    "name":"chandra sekhar",
    "age":18,
    "course":"python"
}
print(student.popitem())

student = {
    "name": "chandra sekhar"
}
student.setdefault("age",18)
print(student)