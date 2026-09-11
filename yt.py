"""
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


ValueError#pass or fail checker
marks = int(input("enter marks: "))

print("passed:", marks >= 40)

#login validation
correct_username = "admin"
correct_password = "1234"
username = input("enter username: ")
password = input("enter password: ")

print(username == correct_username)
print(password == correct_password)

is_logged_in = True
print(not is_logged_in)

#atm eligibility checker
balance = 10000
withdraw = 5000

print(withdraw > 0 and withdraw <= balance)

#student scholarship eligibility checker
mark = float(input("enter marks :"))
attendance = float(input("enter attendance: "))

eligible = marks >= 85 and attendance >= 75

print("schoiarship eligible:", eligible)


#bitwise operators
a = 7
b = 4

print(a & b)
print(a | b)
print(a ^ b)
print(a << b)
print(a >> b)

#electric city bill calculator
units = int(input("enter electricity units: "))

rate = 6

bill = units * rate

print("electricity bill:", bill)

#travel expense calculator
travel = float(input("travel expence: "))
food = float(input("food expence"))
hotel = float(input("hotel expence"))

total = travel + food + hotel

print("total expence:", total)

#list  in python
#list in a ordered and changeable collection that can store a multiple values
marks = {80, 90, 75, 85}

print(marks[0])
print(marks[1])
print(marks[3])


#change elements in a list
marks [80, 90, 75]

marks[1] = 95

print(marks)
#add elements to a list
marks = [80, 90, 75]

marks.append(85)

print(marks)
#remove elements from a list
marks = [80, 90, 75]

marks.remove(90)

print(marks)

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

numbers = [10, 20, 30]

numbers.clear()

print(numbers)


numbers = [10, 20, 30]

print(numbers.index(30))

numbers = [10, 20, 20, 30, 20]

pint(numbers.count(20))

number.sort()

print(numbers)

numbers.sort(reverse=true)

print(numbers)

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

a =  [1, 2, 3]

b = a.copy()

print(b)

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])


#tuples in python
#tuples is a collection of multiple values that is ordered and cannot be changed after creation

student = ("yaswanth", 98, "python")

print(student[0])
#access values in a tuple
student = ("yaswanth", 21, 85.5)

print(student[0])
print(student[1])
print(student[2])

#immutable nature of tuples
student[1] = 22

#tuples are immutable, meaning they cannot be changed after
numbers = (10, 20, 20, 30, 20)

print(numbers.count(20))

numbers = (10, 20, 30, 40)

print(numbers.index(30))

numbers = (10, 20, 30, 40)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#sets in python
#set is a collection of unique values that is unordered and muttable
numbers = {10, 20, 30, 20, 10}

print(numbers)

#suppose students have salected subjects
subjects = {"python", "java", "python", "SQL", "java" }

print(subjects)

#add values to a set
subjects = {"python","java"}

subjects.add("SQL")

print(subjects)
"""
#remove values from a set
subjects.remove("java")

print(subjects)

#sets do not allow dulicate values
numbers = {1, 2, 2, 3, 3, 4}

print(numbers)

