#Q1 

# taking input from user 
a = input('Enter strirg = ')

# printing first character of the string 
print( f" \n first character of the string = {a[0]}")

# printing last  character of the string 
print(f"\n last character of the string = {a[-1]}")

# printing 3rd character of the string 
print(F" \n 3rd characte of the string = {a[2]}")

# printing last 2nd character of the string 
print(f" last 2nd character = {a[-2]}")

#in indexing -ve numbers denotes the end of the string , 
# they are used to print the string from the right hand side 
# and +ve numbers are used to print the string from the left hand side 
# +ve numbers start from 0 , so first character has 0th position and soo on 


#Q2

# taking input from user 
a1 = input('Enter strirg = ')

# printing first 5 character of the string 
print(f' first 5 character of the string = {a1[0:5]}')

# printing first 4 character of the string 
print(f' first 4 character of the string = {a1[0:4]}')

# printing reverse string 
print(f' string reversed = {a1[::-1]}')

# printing every 2 character of the string 
print(f' every 2 character of the string = {a1[::2]}')

# syntax of slicing is variable name [ start : stop : step ]

#Q3

#main string 
ms = input("\n enter the main string = ").lower()
 
# sub string 
ss =  input( "\n enter the sub string = ").lower()

# cheacking if the condions match
if ss in ms :
    print( f" { ss } is present in the { ms }")
elif ss not in ms :
    print(f"\n {ss } is not present in the {ms}")
else:
    print( "invalid input !!")

#Q4 

# taking input from user 
a3 = input('Enter strirg = ')
length = len(a3)
if a3> 0 :

    # length of the string
    print(f" \n length of the string {length}")
    

# last character 
print(f" last character = {a3[length -1]}")

if length % 2 != 0:
    # middel character
    middle = length // 2 
    print(f"middle characer of the string = {a3[middle]}")
else:
    print(" string is even so there is no middle character ")

#comman mistakes while using len() is using it on an empyt string which causes error 

#Q5 

# printing num 0-10
for i in range(11): print(i)

# printing num 5-15
for i in range(5,16): print(i)

# printing odd num from 1-21
for i in range(1,22,2):print(i)

# thress forms of range 
#1 range ( stop )
#2 range ( start , stop )
#3 range ( start , stop , step )

#Q6

# num from 20-10 decreasing 
print("num from 20-10 decreasing  = " ,end="")
for i in range(20,9,-1): print(i,"", end="" )

# num from 15-1 decreasing in steps of 2
print("num from 15-1 decreasing with step 2 = ",end="")
for i in range (15,0,-2):print(i,"", end="")

#Q7

#taking input for string 
s = input("enter sring (dont add space instead _ ) = ")

# print each letter of string 
for i in range ( len(s)):
    print(f" { i} letter = {s[i]}")

# string in reverse order 
for i in range(len(s)-1,-1,-1):
    print(s[i],end="")

#Q8

# taking int input
num = int(input("Enter the number = "))

# cheak 1 : present in range (1-51 )
if num in range(1,51):
    print(f" {num} is present in 1 to 50 ")
else:
    print(f" {num} is not present in 1-50 esries ")
# check 2 :  present in range ( 10,100,5)
if num in range(10,100,5):
    print(f"{num} present in 5 multiple from 10 to 100 ")
else:
    print(f"{num} is not present in range (10,100,5)")

#Q9

# first 10 even num 
print("\nfirst 10 even numbers = ", end="")
for i in range (2,21,2): print(i,end="")

# num from 1-30 with step 3 
print("\n multiplication table of 3 = ",  end="")
for i in range(1,31,3):
    print( i , end="")

# making a string 
pp = " PythonProgramming"

#printing Python only
print(pp[:6])
#printing programming only 
print(pp[6:])

# reverse
print(f" Reverse of {pp} = ", end="")
for i in range(len(pp)-1,-1,-1):
    print(pp[i], end="")


#Q10

#taking string inout from user
word = input("Enter the string = ")

#lenght 
print(f"length of the string = {len(word)}")

#printing first half and second half
length = len(word)
half = length // 2
print(f" first half = {word[:half]}")
print(f"second half = {word[half:]}")

# cheaking if python is in word 
if "python" in word.lower():
    print(f" 'Python ' is present in {word}")
else: print( " python is not present in {word}")

#printing string with their indices
for i in range (len(word)):
    print(word[i],' has index =', i)


#reverse string 
print(" Reverse string = ", end="")
for i in range(len(word)-1,-1,-1):
    print( word[i], end="")
