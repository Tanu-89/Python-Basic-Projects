#Q1 using if 

age = int(input("\nEnter ur age = "))
if (age>= 18):
    print( "\nYou are eligible to vote.\n")

#Q2 using if - else

a = int(input("\nenter any no. from 0-100 = "))
if (a%2 == 0):
    print("\nEven number\n")
else:
    print("\nOdd number\n")

#Q3 using if - elif - else 

mks = int(input("\nEnter your marks = "))
if ( mks >= 90):
    print(" Grade A - Excellent \n")
elif ( mks >= 75):
    print(" Grade B - Goood\n")
elif(mks >=60 ):
    print(" Grade c - Average\n")
elif(mks>= 40):
    print("Grade D - Pass\n")
else:
    print(" Fail \n")

#Q4 using for loop

# print all no. from 1-30 
for i in range(0,31):
    print(i)

# print odd no.s from 1-50
for i in range( 0,51):
    if (i%2==0 ):
        print()
    else:
        print(i)

#print sum of all numbers from 1- 15
a1=0
for i in range(0,16):
    a1=i+a1
print(" Sum of all number from 1-15 = ", a)


#Q5 using while loop 

# printing numbers from 1-20
a2 = 0 
while ( a2 >= 20 ):
    print( a2 )
    a2+=1

#print cube of each number 
a3 = 1
while ( a3<=20):
    print( a3**3)
    a3+=1

#Q6 while loop user controlled 

c=0  # to store the result 
print(" To get the answer of the addition type _0_ ")
b= int (input("Enter first no. to add = "))
while b > 0 :
    c= b+c
    b = int(input("Enter another number to add = "))
print(" sum of all numbrs is = ", c)


#Q7 using nested if 

temperature = int(input("enter the temperature in degree celsius = "))
is_rainning = input("Is it raining ? yes/no = ")

# applying the conditions 
if ( temperature > 30 ):
    if( is_rainning == "no"):
        print("Hot day , wear lignt clothes")
    if ( is_rainning == "yes" ):
        print("Hot and Rainny , Carry Umbrela ")
if ( temperature > 15 ):
    if ( is_rainning == "no"):
        print("Cold weaher , wear warm cloaths ")
    if ( is_rainning == "yes"):
        print("Cold and rainy, wear jacket and takeumbrella.")
else:
    print( " Stay Safe and Heatly , Have a nice day")


#Q8 for loop and if - elif - else statement 

for i in range (1,41):
    if ( i % 3 == 0 ):
        print("Fizz")
    else: 
        if (i % 5 == 0):
            print("Buzz")
        else:
            print(i)
    if ( i % 3 == 0 and i % 5 == 0 ):
        print("FIZZBUZZ")

#Q9

print ( " 1. Add two numbers\n  2. Subtract two numbers\n  3. Multiply two numbers\n  4. Divide two numbers\n  5. Exit")
a4 = int ( input ( " choose anyone Number form above to perform the respective task = "))
while a4!=5:
    if ( a4 == 1):
        print( " you choose additon operatin \n") 
        print( "To exit addiotin operation enter _0_")
        result = 0 
        b= int ( input("enter first no. to add = ")) 
        while b > 0:
            result = b + result 
            b= int ( input("enter another no.  to add = ")) 
        print(" Result = ", result)
    
    # substraction code 
    print ( " 1. Add two numbers\n  2. Subtract two numbers\n  3. Multiply two numbers\n  4. Divide two numbers\n  5. Exit")
    a4 = int ( input ( " choose anyone Number form above to perform the respective task = "))
    if (a4==2):
        print( " you choose substraction operatin \n") 
        print( "To exit substraction operation enter _0_\n")
        result1 = int(input(" enter the fist no. = ")) 
        b1= int ( input("\nenter second no.  = ")) 
        while b1 > 0:
            result1 =result1 - b1
            b1= int ( input("\nenter another no.  to be substracted = ")) 
        print("\n Result = ", result1)

    #multiplication code 
    print ( " 1. Add two numbers\n  2. Subtract two numbers\n  3. Multiply two numbers\n  4. Divide two numbers\n  5. Exit")
    a4 = int ( input ( " choose anyone Number form above to perform the respective task = "))   
    if (a4==3):
        print( " you choose multiplicatin operatin \n") 
        print( "To exit substraction operation enter _0_")
        result = 1 
        b= int ( input("enter first no. to multiply = ")) 
        while b != 0:
            result = b * result 
            b= int ( input("enter another no.  to multiply = ")) 
        print(" Result = ", result)

    #division code 
    print ( " 1. Add two numbers\n  2. Subtract two numbers\n  3. Multiply two numbers\n  4. Divide two numbers\n  5. Exit")
    a4 = int ( input ( " choose anyone Number form above to perform the respective task = "))   
    if (a4 == 4):
        print( " you choose multiplicatin operatin \n") 
        num1 = int (input("Enter the Divident / number to be divided = "))
        num2 = int(input("Enter the Divisor / by which number is going to be divided = "))
        result2 = num1 / num2 
        print(f" {num1 } / {num2} = {result2}")
print ( " You have exited the calculaor , thank you")    


#Q10  debuged code


num = int(input("Enter a number: "))
if num > 100:
    print("Large number")
elif num > 50:
    print("Medium number")
else:
    print("Small number")
count = 1
while count < 10:
    print(count)
    count += 1