'''
name = "Tanishq Balasaheb Mane "
age = 18
height = 1.7
student = True 
print("\n Name of the student =",name )
print("\n Age of the student =", age )
print("\n Height of the student =",height )
print("\n datatype of name=",type(name))
print("\n datatype of age =", type(age))
print("\n datatype of height =",type(height))
print("\ndatatyoe if student =",type(student))
'''
#name- denots that it has string value of someones name 
#age- denotes thist it has integer value of somones age 
# height- denotes it has float value of someones height 
#student- denotes that wether someone is student or not in boolean

#taking variables
''' 
int_a= 35
float_a= 3.5
str_a = "hello python"
bool_a = True 
# printing variables and thier datatypes 
print(f"\n Interger variable = {int_a} , datatype = {type(int_a)}")
print(f"\n Float variables = {float_a} , datatype = {type(float_a)}")
print(f"\n String variable = {str_a}, datatype = {type(str_a)}")
print(f"\n Boolean variable = {bool_a}, datatype ={type(bool_a)}")
# converting Float -> Interger -> Float 
print(f"\n Interger to Float = {int(float_a)}")
print (f"\n float to Interger ={float(int_a)}")
'''

#Taking input 
'''
a= int(input("enter no from 1-20 = "))
b= int(input("Enter no. from 1-20 = "))

add = a+b 
sub = a-b 
mul = a*b
div = a/b
f_div = a//b 
expo = a ** b 
print ( f" additon = {add}")
print(f" substraction = {sub}")
print(f" division = {div }")
print(f"  multiplication = {mul}")
print(f"floor division ={f_div}")
print(f"exponentional no. ={expo}")
# / division gies output as quotient 
# // floor division gies the remainder as the output
'''

'''
x=25
y=30 
z=25
print(f" is x greater than y = {x>y}")
print(f" x equal to z = {x==z} ")
print(f" is x lesss than or equal to y AND y is not equal to z = {x<y and y!=z}")
print(f" is x greater than y OR x equal to z = {x>y or x==z}")'''
'''
b_year = int (input("enter birth year = "))
name = input("Enter name = ")

c_age = 2026 - b_year
print (f"{name} , your birth year is {b_year} , and you are {c_age} years old ")     '''
# we need to change the datatype of the input of birth year , 
# cause input() always takes input in string datatype



'''

w= int(input("enter ur weight in Kg = "))
h= float(input("Ente ur height in meters = "))
bmi = w/(h**2)

print(f" YOUR BMI is {round(bmi,2)}")'''



# Area of the Rectangle = Length x Breadth
#we takes 2 different variables to store values of length and breadth of rectangle 

#l = int(input(" Enter length of the rectangle = "))
#b = int(  input(" enter breadth of the rectangle = "))
 
''' now lets calculate the area of the rectangle 
    for that we takes another variable as area to store the value of the ares of the rectangle 
'''
#area = l*b 

#printing area of the rectangle 

#print(f" length and breadth of rectangle = {l , b} , area of the rectangle = {area} ")

''' perimeter of the rectangle = 2 (l+b)
    taking variable peri for perimeter 
'''
#peri = 2*(l+b)

#printing perimeter 

#print(f" length and breadth of rectangle = {l , b} , perimeter of the rectangle = {peri} ")
'''
Fruits =["mango", "apple", "banana", "cherry"] 
score = 50
print ( f" fruits = {Fruits} , \n score = {score}")
mango_p = "mango" in Fruits 
grapes_p = "grapes" in Fruits

score += 25
print(f" Is mango present in Fruits = {mango_p} ,\n Is grapes present in Fruits = {grapes_p} ,\n Updated score = {score}")
'''
'''
# step 1 : Gather and store information at one place 
name = input (" Enter your ful name = ")
age = int(input("Enter your age = "))
city = input("Enter your city name = ")
s1= int(input("Enter marks obtain in Mathematics = "))
s2 = int (input("Enter marks obtain in Science = "))
s3 = int(input("Enter marks obtain in Social Studies = "))

# step 2 : calculate the marks and percentages
total_mks= s1+s2+s3
percent = (total_mks / 300)*100

# step 3 : Display all information 
print("\n\n------------------  Student Profile ------------------\n\n")
print(f" Name of the Student = { name }")
print(f" Age of the student = {age}")
print(f" City of the education = {city}")
print(f" Total Marks obtain in Mathematics , Science and Social Studies = {total_mks}")
print(f" Percentage obtain = {percent}")          '''




Name = "Alice"
age = 20       # = equal to sign was missing 
city = "Amsterdam"    # "" doubble inverted comma's were missing 
print("My name is" , Name)  # instead of , comma + plus sign was given / plus sign works in java not in python
print("I am", age , "years old")  # commas , after and before age was missing or 
# print(f"I am {age} years old ) this is aslo an method to solve this error
print("I live in " ,city) # comma , was missing before city 
# Check if age is greater than 18 and print message
print("Adult:", age > 18) # comma was missing before the condition 