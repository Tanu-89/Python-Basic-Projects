# Q1

#creating class - Car
class Car :
    #car class constructor , taking brand and model paramenters 
    def __init__(self,brand , model ):
        # making the parameters globa for the classs car
        self.brand = brand 
        self.model = model 
    # method of the class , that prints the model and brand of the car 
    def display_model (self):
        print(f"\n model = {self.model} ")
        print(f" brand = {self.brand}\n")

# creating an object of the class
sedan = Car("M4", "BMW")

#calling the display method of the class 
sedan.display_model()


#Q2


#creating the class Book
class Book:
    # constructor that takes title , author and price as parameters
    def __init__(self, title , author , price):
        # making the parameters global fo rthe class
        self.title  = title
        self.author  = author
        self.price = price
    
    # show method that prints all info abt the book
    def show_details(self):
        print(f"\nName of the book - {self.title}")
        print(f"Name of the author - {self.author}")
        print(f"Price of the book - {self.price}\n")

# creating the object of the class
b1 = Book("One Piece", "Eiichiro Oda", 400)
b2 = Book("Death Note", "Tsugumi Ohba", 419)
# caling show_details method of class books
b1.show_details()
b2.show_details()


#Q3

# creating a clas
class BankAccount :
    def __init__(self , account_holder , balance):
        self.acc_holder = account_holder
        self.balance = balance
    
    # creating the deposit method 
    def deposit(self , amount ):
        #adding the amout to the balance
        self.balance += amount
        print("\n successfully deposited !!")
    
    #creating the withdraw method 
    def withdraw(self, amount):
        # amount shound be lower than the balance 
        if amount > self.balance:
            print("\n Insuffucient Balance !!")
        else:
            self.balance -= amount 
            print('\n amount withdrawal successfull ')
    
    # creating a show balnce method 
    def show_balance (self):
        # prints the balance 
        print(f"\n Ur current balance = {self.balance}\n")
    
# creating an obj

tanu = BankAccount("Tanishq Mane", 7946)

#withdrawing amount from the acc 
tanu.withdraw(342)

#depositing amount in acc
tanu.deposit(6000)

# cheaking the remaing balance 
tanu.show_balance()


#Q4

# creating class Student 
class Student:
    # taking parameteres 
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # method to claculat grades 
    def calculate_marks(self,):
        if self.marks >= 40:
            print(f"\npass")
        else:
            print("\n fail")
        
#creating obj of students 
stud1 = Student("Tanishq" , 78)
stud2 = Student ("sumit", 20)
stud3 = Student("tanu", 67)

stud1.calculate_marks()
stud2.calculate_marks()
stud3.calculate_marks()


#Q5


#class emloye
class Employee:
    # giving parameters
    def __init__(self , name , salary):
        # making parameteres global for class
        self.name= name
        self.salary = salary
    #method that displays employee details
    def diaplay_details(self):
        print(f"\n name of the employee = {self.name}")
        print(f"\n salary = {self.salary}")
    # method that gives rais to the emplyee
    def give_rise (self , amount):
        # giving rais to employee
        self.salary += amount 
        print(f"\n new salary = {self.salary}")
    #mehtod that returns the yearly bonus of the employee
    def yearly_bonus (self):
        return 10/100*self.salary

# creting an emplyee obj
e1 = Employee("Tanu", 50000)

# printing yearly bonus of the employee
print(f"\nyearly bonus = {e1.yearly_bonus()}")

#displaying details of the employeee
e1.diaplay_details()

# giving rais to the employee
e1.give_rise(4000)


#Q6


#mobile class 
class Mobile_Phones:
    # taking parameters 
    def __init__ (self, brand , model , battery_percentage):
        # setting class global variables
        self.brand = brand 
        self.model = model 
        self.battery = battery_percentage

    #  method that incereases battery %
    def charge(self ,percent):
        # increasing battery %
        self.battery += percent

    # method to reduce battery % over use 
    def use_phone(self, minutes):
        a = minutes // 10
        self.battery -= a 

    # method that shows current battry status
    def show_status(self):
        print(f"\n current status = {self.battery}")

m1 = Mobile_Phones("samsung" , "A20" , 89)

m1.charge(11)
m1.show_status()
m1.use_phone(400)
m1.show_status()


#Q7

# class rectangle
class Rectangle  :
    # taking parameters length and width 
    def __init__ (self , length , width):
        # making parameters global for class
        self.lenght = length
        self.width = width
    # calculating are of the rectangle 
    def area(self):
        self.area= self.width*self.lenght
        return self.area
    # calculating perimeter of tha rectangle
    def perimeter(self):
        self.perimeter= 2*(self.lenght+self.width)
        return self.perimeter
    # displaying the area and persimeter of the rectangle
    def display (self):
        print(f"\n area of the rectangle  = {self.area}")
        print(f"\n perimeter of the recangle = {self.perimeter}")


# creating obj of rectangle
r1 = Rectangle(7, 9)
# calculating area
r1.area()
# calculating perimeter
r1.perimeter()
# printing area and perimeter 
r1.display()


#Q8

#class player 
class Player :
    # taking parameteres and making them global for class
    def __init__ (self , name , score , level):
        self.name = name 
        self.score = score
        self.level = level

    # increasig score 
    def incerease_score(self, points):
        # adding points to score
        self.score += points

    # leveling up by 1 
    def level_up(self):
        self.level += 1
    
    # showing progress 
    def show_progress(self):
        print(f"\n player name = {self.name}")
        print(f" player score = {self.score}")
        print(f" player level = {self.level}\n ")

# creating an obj
p1 = Player("d3v17_lucifer", 6849 , 56)

# leveling up player 
p1.level_up()
p1.level_up()
p1.level_up()
p1.level_up()
p1.level_up()
p1.level_up()
p1.level_up()

# increasing players score 
p1.incerease_score(6754)

# cheaking status
p1.show_progress()


#Q9


class Person:
    def __init__(self , name, age):# needs intendation , self parameter missing 
        self.name = name# 
        self.age = age
    def introduce(self):#self missing in parameter , intendation missing  
        print("\n My name is" , self.name , "and I am" , self.age , "years old. \n ")
    # commas before and after variables are missng , self. missing for the variables
    # needed intendation

p1 = Person("Rahul", 25)
p1.introduce()



#Q10


# Simple Library Management System
class Books:
    #class takes parameter title and author , and status is set to available 
    def __init__(self, title , author , status= "Available"):
        # all parameters are global for class
        self.title = title
        self.author = author
        self.status = status
    # method that issues book     
    def issue_book(self):
        # once book is issued  , status changes 
        self.status= "Issued"
        print("\n Book issued successfully ")
    # method that returns the book 
    def return_book(self):
        # once book is return , status is changes
        self.status= "Available"
        print("\n Book sccessfully return ")
        print("\n Book is now available ")
    # method tht shows all info of book
    def show_info(self):
        print(f"\n Name of the book = {self.title}")
        print(f" Name of the author = {self.author}")
        print(f" Book status = {self.status}")

# creating list to store books
library = []

# adding books to library 
library.append(Books("hello", "rahul"))
library.append(Books("nice to meet you", "samiksha"))
library.append(Books("destroyer", "tanishq"))
library.append(Books("alcoholic", "jaya"))

# pirnting menu 
while True:
    print("\n ------------  Library Management System ----------------")
    print(" 1 = add a new book")
    print(" 2 = issue a book")
    print(" 3 = return a book ")
    print(" 4 = show all books")
    print(" 0 = exit ")

# taking the task choise 
    a = int(input("Enter choise : "))
# performing 1st task 
    if a == 1 :
        title=  input("\n Enter title = ")
        author = input("\n Enter author name = ")
        # adding a new book to the library 
        library.append(Books(title , author))
        print("\n Book added successfully ")
# performing 2nd task 
    elif a == 2:
        title = input("\n enter book title = ")
        found = False
        for book in library:
            if title.lower() in book.title.lower():
                book.issue_book()
                found = True
                break
        if not found:
            print("\n book not found ")

    elif a == 3 :
        title = input("\n enter book title = ")
        found = False
        for book in library:
            if title.lower() == book.title.lower():
                book.return_book()
                found = True
                break
        
        if not found:
            print("\n book not found ")

    elif a == 4 :
        if len(library) == 0 :
            print("\n no book in library ")
        else:
            print("\n ===== Book list  =====")
            for book in library:
                book.show_info()
    
    elif a== 0 :
        print("thankyou for using Library Management system ")
        break
