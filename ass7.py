#Q1

#A tuple with 5 numbers using parentheses.
tup=(1,6,3,8,4)

#A mixed tuple containing integer, string, float, and boolean.
tup1=(69, "vedu", True, 8.9 )

#An empty tuple using two different ways.
# 1
tup2=()
# 2
tup3=tuple()

#A single-element tuple with the value 99.
tup4=(99,)
''' 
single element tuple needs to have comma after the element or the pytho treatees it as integer not tuple
'''
#printing all tuples and their types 

print(f"\n tup={tup}, type = {type(tup)}") 
print(f"\n tup1={tup1}, type = {type(tup1)}")
print(f"\n tup2={tup2}, type = {type(tup2)}")
print(f"\n tup3={tup3}, type = {type(tup3)}")
print(f"\n tup4={tup4}, type = {type(tup4)} \n")

#Q2

#Create a tuple without using parentheses (tuple packing) to store: your name, age and city.
tup5 = "tanu" , 18 , "tokoyo"
# ptinting the tuple and its type
print(f"type of {tup5} = {type (tup5)}")

# upacking the tuple
name , age , city = tup5

#printing the unpack tuple
print("Name =", name)
print('Age = ', age)
print('city = ', city)

#Q3

#create tuple
colors = ('red', 'green', 'blue', 'yellow', 'purple', 'orange')

# 1st element 
print(f"first element = {colors[0]}")

# 2nd element
print(f"second element = {colors[1]}")

# last element 
print(f"last element = {colors[-1]}")

# 2nd last element 
print(f"2nd last element = {colors[-2]}")

# taking index rom useer and printing the element on that index
a= int(input("enter the number from 0-5"))
print(f"element at {a } index = { colors [a]}")


#Q4

#tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

#Elements from index 2 to 7
print(f"Elements from index 2 to 7 = {numbers[2:7]}")
#First 5 elements
print(f"First 5 elements = {numbers[:6]}")
#Last 4 elements
print(f"Last 4 elements = {numbers[-4:]}")
#Every second element
print(f"every 2nd element = {numbers[::2]}")
#The entire tuple in reverse order
print(f"tuple in reverse = {numbers[::-1]}")
#slicing syntax.
'''
tuple_name[start:stop:step]
'''


#Q5


#nested tuple to represent a 3x3 matrix:
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# The first row
print(f"first row = {matrix[0]}")
# The element at second row, third column
print(f"element at 2nd row third coloum = {matrix [1][0]}")
# The element at third row, first column 
print(f"element at 3rd row first coloum = {matrix [2][0]}")


#Q6

#creaing tuple
student = ('Rahul', 20, 'Computer Science', 'A')

# Iterate through the tuple using a for loop and print each item.
for i in student:
    print(f"element of tuple = {i}")
# Unpack the tuple into four variables (name, age, branch, grade) and print themwith descriptive messages.
name, age, branch, grade = student
print(f"name in tuple = {name}")
print(f"age in tuple = {age}")
print(f"branch in tuple = {branch }")
print(f"grade in tuple = {grade}")

#Q7

#creat tuple
grades = ('A', 'B', 'A', 'C', 'A', 'B', 'D', 'A', 'B')

#Count and print how many times 'A' appears.
print(f"A in the tuple has occured {grades.count('A')} times")

# Count and print how many times 'B' appears.
print(f"B in the tuple has occured {grades.count('B')} times")

# Take a grade as input from the user and print how many times it appears.
a1= input("enter any grade from A - D = ")
print(f" {a1} has appeared {grades.count(a1)} times")


#Q8

#create tuple
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'apple')

#Find and print the first index of 'banana'.  
print(f" index of the 'banana' in tule is = {fruits.index('banana')}")  

# Find and print the first index of 'banana' starting the search from index 2.
print(f" index of the 'banana' in tule is = {fruits.index('banana',2)}")  

# Use try-except to safely find the index of 'kiwi' and print "Not found" if it doesn't exist.
try:
    print(f" kiwi found at the {fruits.index('kiwi')} index ")
except ValueError:
    print("not found")



#Q9

#tuple
coordinates = (10, 20)
print(f" original tuple = {coordinates}")

# Change the first element
'''coordinates[0]=30'''
'''
TypeError: 'tuple' object does not support item assignment
'''
#Add a new element using append()
'''coordinates.append(50)'''
'''
AttributeError: 'tuple' object has no attribute 'append' 
'''

'''correct way to change the tuple 
'''
# convert tuple to list 
tlist= list(coordinates)
# change the first element 
tlist[0]= 90
#appending a num 
tlist.append(60)

#converting the list back to tuple
coordinates= tuple(tlist)
# printing the chaged tuple
print(f" updated tuple = { coordinates}")

#Q10 SRP 

#taking input from user
name = input("Enter name = ")
roll_no= int(input(" Enter Your roll no = "))
sub1= int(input("Enter the marks of subject 1 = "))
sub2 = int(input("Enter the marks of the subject 2 = "))
sub3 = int(input("enter marks of subject 3 = "))

# storing all info in tuple 
data = name, roll_no , sub1 ,sub2, sub3

# printing the whole record 
print(f" all detils of student = { data}")

# upacking the tuple and printing indivisually
Name , roll, s1, s2 ,s3 = data 
print('name = ' , Name)
print(f"roll number = {roll}")
print(f" subject 1 = {s1}")
print(f" subject 2 = {s2}")
print(f" subject 3 = {s3}")

# check how many times a particular mark appears
mks = int(input( " Enter marks to count = " ))
marks= (s1,s2,s3)
if mks in marks :
    print(f" Marks {mks} has appeared {marks.count(mks)} times")
else: 
    print(f"It hasn't appear")



# taking student datas 
name1 = input("enter name of the student = ")
rollno1 = int(input("enter the roll no. of student = "))
sb1= int( input("enter the marks of 1st subject = "))
sb2 = int(input("enter the marks of 2nd subject = "))
sb3 = int(input("enter the marks of 3rd subject = "))

studtup = (name1 , rollno1, sb1, sb2 , sb3)

name2 = input("enter name of the student = ")
rollno2 = int(input("enter the roll no. of student = "))
sb4= int( input("enter the marks of 1st subject = "))
sb5 = int(input("enter the marks of 2nd subject = "))
sb6 = int(input("enter the marks of 3rd subject = "))

studtup1 = (name2 , rollno2, sb4, sb5 , sb6)

stud = studtup , studtup1

print(f"Data of multiple studends = {stud}")