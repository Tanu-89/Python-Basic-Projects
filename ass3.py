#Q1

#functions are very important in python , they makes the code reuseable and easy to understand 
#funchions also reduces the coplexsity of the program 

def welcome():
    print("\n\n Welcome to Python\n\n")
welcome()

#Q2

def greet(name):
    print(f"Hello , {name}! welcome back ")

#caling the fun with my  name 
greet("Tanishq")

#caling the fun with other name 
greet ("samiksha")

#Q3

def show_message(message="Hello"):
    print(message)

#without paramenter
show_message()

#with differen parameter 
show_message("welcome")

# default parmenters hepls keep the code flexiblity and it hepls in code consistency 
#even if the user omits the parametes it dosent effect the program

#Q4

def add ( a, b ):
    return a+b

print( add( 4,7 ))

def add1(a,b):
    print(a+b)
add1( 8,2 )

#retun in a fuction returns the final value or the executed values of the funvtion 
# print statement prints the output of the function on the terminal or console 

#Q5

 
def student_info(name, age):
    print(f" name = {name}, age = {age}")

#positional arguments
student_info("Tanishq " , 18)
student_info(18 , "Tanishq")

#keyword argumennts 
student_info(age=21, name="samiksha")

# Inpositional arguments , order of the argument passing  matter so much , 
# the first patameter goes to the first argument and second to the second , and soo on 
# In keyword aruments values are passed by their arguments , therefore their order dont matter 

#Q6

# prints the square of the number 
def square(num):
    print(f" square of the {num}= {num**2}")

# prints the cube of the number
def cube(num):
    print(f" cube of the {num} = { num**3}")

num= int(input(" Enter the number = "))

square(num)

cube(num)

#Q7 
 
def countdown(n):
    if n == 0:
        return 0
    else:
        print(n)
        countdown(n-1)
 
print(f" Countdown starts = ")
countdown(10)


#Q8 

def factioral(n):
    if n==0: # the base condition is used to exit recursion , when the value of n gets to 0 recursion breakes 
        return 1
    elif n==1: # this condiont is put because the factorial of 1 is 1 
        return 1
    else: # here the factorial is calculated and returned 
        return n*factioral(n-1)
n = int(input("Enter number = "))
print(f" factorial of {n} = { factioral(n)}")


#Q9

total = 0 
def add_value(x):
    global total 
    total = total + x 
    print(f" Total +{x} = { total}")
add_value(3)
add_value(4)
add_value(7)
add_value(2)


#Q10

#takes input from user and returns it 
def get_number():
    number=int(input("Enter value = "))
    return number

# checks if the given numbe is even or odd 
def is_even(n):
    if n % 2 == 0 :
        return True
    else:
        return False
    
# It returns the number with the power of 2 , default exp = 2
def power(base, exp=2):
    return base**exp

# prints wether the given number is even or odd along with its square 
def show_result(num):
    if is_even(num):
        print(f"{num } is an even number")
    else:
        print(f"\n {num } is an odd number ")
    print(f" Square of {num} = { power(num)}\n")
print(" to terminate the process enter 0")

# while loop is used to take multiple inputs consecutively 
while True:
    b= get_number()
    # this is to stop the program
    if b== 0:
        break
        print(" Terminated the process ")
    else:
        show_result(b)
