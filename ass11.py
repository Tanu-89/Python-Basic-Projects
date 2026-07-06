#Q1

# taking two nos. as input from user
try:
    a= int(input("Enter number = "))
    b = int(input("Enter number = "))
    print(a/b)
# catching error in case wrong input was given
except ValueError:
    print(" \n incorrct input ")


#Q2


# zero division error
try:
    a = int(input(" \n Enter a number to divide = "))
    b = int(input(" Enter a number to be divided = "))
    print(f"\n division = {a/b}")

#catching zero division error
except ZeroDivisionError:
    print("\n Error: Division by zero is not allowed ")


#Q3



# taking inputs 
try :
    a= int(input("\n Enter number = "))
    b = input("enter a numer = ")
    b= int(b)
    print("Division = ", a/b)
# catching value error exception
except ValueError:
    print(" \n Error :  wrong input entered ")

# catching zero division error
except ZeroDivisionError:
    print("\n Error : division by 0 is not allowed ")


#Q4


# taking input of two numbers and dividing them 
try:
    a = int(input("Enter a number = "))
    b= int(input("Enter a number ="))
    print(a/b , " is the division ")
 
# handling value error 
except ValueError:
    print(" Error : enter only digits  ")

# else executes when error dosent occurs
else:
    print(" division Performed Successfully ")


#Q5

# taking inputs of 2 numbers 
try :
    a = int(input("Enter num = "))
    b = int(input("enter num = "))
    print(a+b)

# handlling wrong input error
except ValueError:
    print("Error : Enter only digits ")

finally:
    print("Program execution completed.")

# finally block always runs , even if there is an error in the program 


#Q6


#try block , taking inputs from user 
try:
    a= int(input("\n Enter num1 = "))
    b= int(input("Enter num2 = "))
    print("division = ", a/b)

#except block , handling error
except ValueError:
    print("\n Enter only numbers ")

except ZeroDivisionError:
    print("\n divion by zero is not allowed ")

# else block runs when no errors occur
else:
    print(" code executed successfully ")

# finally always runs wether there is an error or not 
finally:
    print("this block runs always ")
    


#Q7


# taking age input
try:
    # taking input as integer
    age =  int(input("\n Enter age = "))
    print("\n Your age is ",age)
    # raising error when entered - ve numbers 
    if age < 0 :
        raise ValueError
# handling error 
except ValueError:
    print("\n Age cannot benegative.")



#Q8

# taking number as an input
try:
    num= int(input("\n Enter number = "))
    div = 100/num

# handlling exception 
except ValueError , ZeroDivisionError:
    print(" Error : wrong input , enter number, it should be greater than 0 ")

# printitng division in else block 
else:
    print(f"\n division = {div}\n ")


#Q9

try:       # colon missng 
    # indentation missing
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:      # colon missing 
    # indentation mising 
    print("Please enter a valid number")
    
except ZeroDivisionError:       # argument mising 
    # indentation mising
    print("Some error occurred")



#Q10



# making the loop run till the end 
while True:
    # printing the menu 
    print("\n -------------  Calculator -----------")
    print("Enter 1 for Addition ")
    print("Enter 2 for Substraction ")
    print("Enter 3 for Multiplication ")
    print("Enter 4 for Division ")
    print("Enter 0 to exit calculator \n")
    # taking input
    try:

        choise = int(input("\n Enter ur choise = "))
        # in case if unexpected number is entered
        if choise > 4 or choise < 0:
            # raising error when entered unexpected number
            raise ValueError
    # handling errors 
    except ValueError :
        print(" Enter choise from the below menu , and digits only ")
    
    # performing Addition 
    if choise == 1 :
        try:
            print( "\n========= Additon ==========")
            # taking inputs 
            num1 = int(input("\n Enter 1st number = "))
            num2 = int(input("\n Enter 2nd number = "))
            # adding numbers 
            result = num1 + num2
        # handling Error 
        except ValueError:
            print("\n Enter a only numbers ")
        # printing the result
        else:
            print(f"\n Addition = {result}")
        # printing operation attempted 
        finally:
            print("Operation attempted.")
    elif choise == 2 :
        try :
            print("\n ========== Substraction =========")
            # taking inputs 
            num1 = int(input("\n Enter greater number = "))
            num2 = int(input("\n Enter smaller number = "))
            # substracting num1 from num2
            result = num1 - num2
        # handling exception 
        except ValueError:
            print("\n Enter a only number ")
        # printing the result
        else:
            print(f"\n Substraction = {result}")
        # printing operation attempted 
        finally:
            print("Operation attempted.")    

    # performing Multiplication
    elif choise == 3:
        try:
            print("\n ========== Multiplication =========")
            # taking inputs 
            num1 = int(input("\n Enter 1st number = "))
            num2 = int(input("\n Enter 2nd number = "))
            # multiplying numbers 
            result = num1*num2

        # handling error
        except ValueError:
            print("\n Enter a only number ")
        # printing the result
        else:
            print(f"\n Multiplication = {result}")
        # printing operation attempted 
        finally:
            print("Operation attempted.") 
    # performing Division 
    elif choise == 4:
        try :
            print("\n ========== Division =========")
            # taking inputs 
            num1 = int(input("\n Enter 1st number = "))
            num2 = int(input("\n Enter 2nd number = "))
            # dividing num1 by num2 
            result = num1/num2

        # handling error
        except ValueError , ZeroDivisionError:
            print("\n Enter a only number , and above 0 ")
        # printing the result
        else:
            print(f"\n Division = {result}")
        # printing operation attempted 
        finally:
            print("Operation attempted.") 
    # exisiting the loop
    elif choise == 0 :
        print("\n you choose to exit the calculator ")
        break