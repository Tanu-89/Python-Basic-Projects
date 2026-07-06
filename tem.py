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