
#comparison operators
a = 10
b = 20

print(a == b)
print(a != b )
print(a > b )
print(a < b )
print(a <=b )
print(a >=b )


#age eligibility checker
age = int(input("enter your age:"))

print("eligibility:", age >= 18)

#pass or fail checker
marks = int(input("enter marks:"))

print("pass:", marks >= 40)

#login validation
correct_username ="admin"
correct_password ="1234"

username = input("Enter username: ")
password = input("Enter password: ")

print(username == correct_username)
print(password == correct_password)

#logical opertors
age = 25
citizen = True

print(age >= 18 and citizen == True)

age = 16
citizen = True

print(age >= 18 and citizen == True)

has_card = False
has_cash = True

print(has_card or has_cash)

is_logged_in = True

print(not is_logged_in)

#atm eligibility checker
balence = 1000
withdraw = 5000

print(withdraw > 0 and withdraw <= balence)

#student scholarship eligibility checker
marks = float(input("Enter marks"))
attandence = float(input("enter attendence"))

eligible = marks >= 85 and attandence >= 75

print("scholarship eligible:", eligible)

#identity operators
a = None

print(a is None)
print(a is not None)

#bitwise operators
a = 5
b = 3

print(a & b)
print(a | b)
print(a ^ b )
print(a << b)
print(a >> b)


#electric city bill calculator
units = int(input("Entr electricity units:"))
rate = 6
bill = units * rate

print("electricity bill:", bill )


#travel expence calculator
travel = float(input("Travel expences: "))
food = float(input("food expences: "))
hostel = float(input("hostel expences: "))
total = travel + food + hostel

print("Total Expences:" , total)


#list in python
#list is an ordered and changeable collection that can store
marks = [80, 90, 75, 85]

print(marks)


#accessing elements in a list

print(marks[0])
print(marks[1])
print(marks[3])

number = [77,69,92,96,79,86,42,67]

print(number[2])
print(number[4])
print(number[6])

#change element in a list
marks = [80, 90, 75]

print(marks)

marks[1] = 95

print(marks)

#add elements to a list
marks = [80, 90, 75]
marks.append(85)

print(marks)


#remove element from a list
marks = [80, 90, 75]
marks.remove(90)

print(marks)


#insert element from a list
number = [10, 20, 30]
number.insert(1, 15)

print(number)

number = [10, 20, 30]
number.insert(1, 15)
number.insert(2, 25)

print(number)


#extended method
a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)

print(a)


#clear method
numbers = [10, 20, 30]
number.clear()

print(numbers)


#index method
number = [10, 20, 30, 40]

print(number.index(30))



#count method
number = [10, 20, 20 ,30, 20]

print(number.count(20))


#sport reverse
number = [40, 10, 30, 20]
number.sport()

print(number)

number.sprt(reverse=True)

print(number)


#reverse method
number = [10, 20, 30, 40]
number.reverse()

print(number)


#copy 
a = [1, 2, 3, 4]
b = a.copy()

print(b)


#list
number = [10, 20, 30, 40, 50]

print(number[1:4])
print(number[:3])
print(number[2:])
print(number[::-1])


#tuples in python
#Tuple is a collection multiple values that cannot be change after creation
student = ("karthik", 98, "python")

print(student[0])


#access values in a tuple
student = ("karthik", 21, 85.5)

print(student(0))
print(student(1))
print(student(2))


#immutable nature of tuple
student = ("karthik", 21, 85.5)
student = 21

print(student)


#tuple are immutable, meaning they cannot be changwd aftee

number = (10, 20, 30)
print(number.index(20))
number = (10, 20, 30, 40, 50)
print(number.index(30))
number = (10, 20, 30, 40)
print(len(number))
print(max(number))
print(min(number))
print(sum(number))


#set in python
#Set is a collection of unique values that are unordered and unindexed

numbers = {10, 20, 30, 20, 10}
print(numbers)

#why use set?

#suppose student have selected subject 

student = {"python", "java", "SQL", "java"}
print(student)


#add values to a set

subject = {"python", "java"}
subject.add("SQL")
print(subject)


#remove values from a set

subject.remove("java")
print(subject)


