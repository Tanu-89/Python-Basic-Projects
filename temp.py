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
