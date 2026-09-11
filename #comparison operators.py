#comparison operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


#age eligibility checker
age = int(input("enter your age:"))

print("eligible:", age >= 18)


#pass or fail checker
marks = int(input("enter marks: "))

print("passed:", marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"
username = input("enter username: ")
password = input("enter password: ")

print(username == correct_username)
print(password == correct_password)

#logical operators
age = 25
citizen = True

print(age >= 18 and citizen == true)
