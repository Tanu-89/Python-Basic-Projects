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

class Employee :
    def __init__(self, emp_id , name, detail):
        self.empid = emp_id
        self.name = name
        self.detail = detail

    def show_detail (self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Department  :", self.details[0])
        print("Salary      :", self.details[1])
        print("---------------------------")


# Dictionary to store Employee objects
employees = {}

# Add 3 employees
for i in range(3):
    emp_id = int(input("Enter Employee ID: "))
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    emp = Employee(emp_id, name, department, salary)
    employees[emp_id] = emp

# Display all employees
print("\nEmployee Details")
for emp in employees.values():
    emp.show_details()



# Q9 


import math

try:
    # Take sentence as input
    sentence = input("Enter a sentence: ")

    # Extract unique words using set
    words = sentence.split()
    unique_words = set(words)

    # Print unique words in sorted order
    print("Unique words in sorted order:")
    for word in sorted(unique_words):
        print(word)

    # Print square of total unique words
    count = len(unique_words)
    print("Total unique words =", count)
    print("Square of total unique words =", math.pow(count, 2))

except Exception as e:
    print("Error:", e)



# Q10


import math
import random

# Dictionary to store history
history = {}
count = 1


# Function for Basic Arithmetic
def arithmetic():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Enter choice: "))

        if ch == 1:
            return a + b
        elif ch == 2:
            return a - b
        elif ch == 3:
            return a * b
        elif ch == 4:
            return a / b
        else:
            print("Invalid Choice")
            return None

    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except Exception as e:
        print("Error:", e)


# Function for Scientific Calculations
def scientific():
    try:
        num = float(input("Enter number: "))

        print("1. Square Root")
        print("2. Factorial")
        print("3. Sine")
        print("4. Cosine")

        ch = int(input("Enter choice: "))

        if ch == 1:
            return math.sqrt(num)
        elif ch == 2:
            return math.factorial(int(num))
        elif ch == 3:
            return math.sin(num)
        elif ch == 4:
            return math.cos(num)
        else:
            print("Invalid Choice")
            return None

    except Exception as e:
        print("Error:", e)


# Function for Random Numbers
def random_number():
    return random.randint(1, 100)


# Main Menu
while True:
    print("\n===== MENU =====")
    print("1. Basic Arithmetic")
    print("2. Scientific Calculations")
    print("3. Generate Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        result = arithmetic()
        print("Result =", result)

    elif choice == 2:
        result = scientific()
        print("Result =", result)

    elif choice == 3:
        result = random_number()
        print("Random Number =", result)

    elif choice == 4:
        timestamp = input("Enter timestamp (e.g. 10-07-2026 10:30 AM): ")
        history[count] = {
            "Timestamp": timestamp,
            "Result": result
        }
        count += 1
        print("Result Stored Successfully.")

    elif choice == 5:
        if len(history) == 0:
            print("No History Available.")
        else:
            print("\nHistory")
            for key, value in history.items():
                print("Record", key)
                print("Timestamp:", value["Timestamp"])
                print("Result:", value["Result"])
                print("-------------------")

    elif choice == 6:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")