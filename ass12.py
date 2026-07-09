# Q1
 
# creating a function that counts vowels and returns the num of count 
def count_vowels(s):
    #putting all vowels in one set 
    vowels = {"a", "e","i","o","u",'A','E','I','O','U'}
    count = 0
    # running the for loop on the vowels
    for char in s:
        # increasig count of the vowels by one ever time there is a match 
        if char in vowels:
            count += 1
    # returning the final count of the vowels
    return count   

# taking input of vowels
s = input("enter word = ")
print("vowels count = ", count_vowels(s))



# Q2


# function analyze_string(s) that takes a string as input and
def analyze_string(s):

    #Prints its length using len().
    print("length of the strign = ", len(s))

    # Prints the string in reverse using slicing.
    print("reverse string = ", s[::-1])

    # Counts and prints how many vowels (a,e,i,o,u) are in the string (case insensitive).
    print("vowels = ", count_vowels(s))

    # Uses a for loop with range() to print each character with its positive and negative index.
    for i in range(len(s)):
        print(s[i], " index = " , i )

#Call this function with user input and handle empty string case.
while True :
    try :
        s= input("Enter string = ")
        if s=="":
            raise ValueError
        
    except ValueError:
        print("Empty string not allowed ")
    else:
        analyze_string(s)
        break



#Q3


# Create a function manage_marks() that:
def manage_marks():

    # defining variables to be used further
    total = 0
    mark_list = []
    high , low = 0 , 100

    # Takes 5 subject marks as input from the user.
    while True:

        # Handles ValueError if non-numeric input is given.
        try:
            marks = int(input("Enter ur marks = "))
        except ValueError:
            print(" Enter only Numbers ")
        else:
            #storing total marks 
            total += marks


            # highest 
            if marks >= high :
                high = marks

            # lowest 
            if marks < low :
                low = marks

            # Stores them in a list.
            mark_list.append(marks)
        # takes only 5 inputs
        if len(mark_list) == 5:
            break

        # Calculates and prints the average, highest, and lowest marks.
    print(f"-- Highest marks = {high}")    
    print(f"-- Lowerst marks = {low}")
    print(f"-- Avg marks = {total//5}")
    print(mark_list)

manage_marks()


#Q4



# Create a class Student with attributes: name, roll_no, and marks_list (a list of marks).

class Student :

    # __init__ to initialize the student.
    def __init__(self, name , roll_no , marks_list):
        self.name = name 
        self.roll= roll_no
        self.ml = marks_list
    
    # add_mark(mark) to add a mark to the list (handle invalid marks).
    def add_mark(self):
        mark = int(input("-- Enter marks to add = "))
        try:
            if mark > 100 :
                raise ValueError
        except ValueError:
            print(" -- Enter valid marks ")
        else:
            self.ml.append(mark)
    
    # get_average() to return the average.
    def get_average(self):
        avg = sum(self.ml) // len(self.ml)
        print("\n-- Average marks = ", avg)

    # display_info() to show all details.
    def display_info (self):
        print(f"-- Name = {self.name}")
        print(f"-- Roll no. = {self.roll}")
        print(f"-- Mark list = {self.ml}")
    

name = input("\n -- Enter name = ")
roll_no = int(input("\n -- Enter roll no = "))
marklist = list()
print("\n when entered all subjects marks , enter 101 \n Enter marks of all subjects")
while True:
   
    marks = int(input("-- Enter marks = "))
    
    if marks == 101:
        break
    else:
        marklist.append(marks)

s1 = Student(name , roll_no , marklist)

# add marks 
s1.display_info()
s1.add_mark()
s1.display_info()
s1.get_average()
s1.display_info()



# Q5

# function student_database() that uses a dictionary (roll number as key) to store student records.

def student_database():
    stud = {}
    while True:
        print("1. Add student (name, age, city)")
        print("2. Search student by roll number")
        print("3. Display all students")
        print("4. Exit")
        try :
            choise = int(input("Enter choise = "))

            if choise == 1:
                roll_no = int(input("Enter roll number = "))
                name= input("Enter name = ")
                age = int(input("Enter age = "))
                city = input("Enter city = ")

                stud.update({
                    roll_no:{"Name":name , "Age":age , "City":city}
                    })
                print("Student added successfully.")
            

            if choise == 2 :
                roll = int(input("Enter a roll no = "))
                record = stud.get(roll)
                if record:
                    print("\nStudent Found")
                    print("Roll Number :", roll)
                    print("Name :", record["Name"])
                    print("Age :", record["Age"])
                    print("City :", record["City"])
                else:
                    print(" Student not found ")
            
            if choise == 3 :
                if len(stud) == 0 :
                    print("No student records available.")

                else:
                    print(" -- Student Records -- ")
                    for roll , record in stud.items():
                        print("--------------------------")
                        print("Roll Number :", roll)
                        print("Name :", record["Name"])
                        print("Age :", record["Age"])
                        print("City :", record["City"])

            elif choise == 4 :
                print('=== Exisiting ===')
                break



# Q6 


import random as rm
import math as m 

set1 = set()
# Takes 10 numbers as input and stores unique numbers in a set.
for i in range(10):
    num = int(input("Enter numbers = "))
    set1.add(num)
# Converts that set into a tuple.
tup = tuple(set1)

# Uses random module to pick and print 3 random numbers from the tuple. 
if len(tup) > 3 :
    random_num = rm.sample(tup,3)
    print(f" 3 random numbers = {random_num}")
else:
    print("unique numbers are less than 3 ")

# Uses math module to print the square root of the sum of the tuple elements.
try :
    total = sum(tup)
    print(f"square root = {m.sqrt(total)}")
except Exception as e :
    print("Error", e)


# Q7

# Create a lambda function to calculate the square of a number.
sqr = lambda x : x**2

try :
     # Generate numbers from 1 to 20 and store their squares
    num1 = list(map(sqr , range(1, 21)))

    print("squares = ", {num1})

    #Prints only the even squares from the list.
    for i in num1:
        if i % 2 == 0 :
            print(i , end=" ")
            
except Exception as e :
    print("Error ", e )# Q7

# Create a lambda function to calculate the square of a number.
sqr = lambda x : x**2

try :
     # Generate numbers from 1 to 20 and store their squares
    l = list(map(sqr , range(1, 21)))

    print("squares = ", l)

    #Prints only the even squares from the list.
    print("even squres = \n [", end=" ")
    for i in l:
        if i % 2 == 0 :
            print(i , end=" ")
    print("]" , end= " ")
except Exception as e :
    print("Error ", e )


#Q8 

