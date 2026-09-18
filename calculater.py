
#reading user input 
base = int(input("enter the base"))
exponent = int(input("enter the exponent: "))
#calculate the power of and print the result
print(base ** exponent)


#Average Of Three Numbers
#Taking 3 integers numbers from user
n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))
n3 = int(input("enter the third number: "))

#find the total 
total = n1+n2+n3
print(total)
#find the Average 
ave = total/3 # Division operator /--> always gives
#print the Average 
print(ave)


#Great Than Comparison
#read 2 integer number from user
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
#check whether the first number is greater than the second number
if a > b:
    print("The first number is greater than the second number.")
else:
    print("The first number is not greater than the second number.")
print("Great than comparison")


#Equality check 
#cheak wherher both numbers are same or not
#If numbers are same  - true
#If numbers are not same - false
n1 = int(input("enter the first number:"))
n2 = int(input("enter the second number:"))
print(n1 == n2)

