#Q1 

# a) An empty dictionary using two different ways.
# 1
dict1 = {}
print(dict1)
print(type(dict1))

#2
dict2 = dict()
print(dict1)
print(type(dict2))

# b) A dictionary with string keys (name, city, course).
info1 ={"name":"tanu" , "city":'pune' , 'course': 'AIML'}
print(info1)
print(type(info1))

# c) A dictionary with integer keys.
integer = {1:"tanu", 2:'manu', 3:'samu'}
print(integer)
print(type(integer))

# d) A mixed data type dictionary (string, int, float).
mixed = {1:'a', 2:8.9 , 3 : 67}
print(mixed)
print(type(mixed))

# syntax : dict_name = {key : value}

#Q2

#given dicionary
student = {
"name": "tanishq",
"age": 00,
"city": "pune",
"marks": 00
}

# Print the value of "name" using square brackets.
print(f"student name = {student['name']}")

#Update the "marks" to 92.
student['age']=92

#Add a new key "grade" with value "A".
student.update({'grade':"A"})

#Print the updated dictionary.
print(" Updated dictionary ")
for i , j in student.items():
    print(f"{i} = {j}")

#Q3

# given
person = {"name": "Priya", "age": 21, "profession": "Engineer"}

print(person.get("age"))
print(person.get("salary"))

#print all keys
print(person.keys())

#print all values
print(person.values())

# print all key values
print(person.items())

#Q4
#given dict 
students = {
"s1": {"name": "Rahul", "age": 20, "marks": 88},
"s2": {"name": "Sneha", "age": 21, "marks": 95}
}
#pritning student 1 values
print(students["s1"])

#pritning student 2 marks
print("student marks = ", students["s2"]['marks'])

students["s1"]["math"]= 90

for i,j in students.items():
    print(f"{i}= {j}")

#Q5
info = {"brand": "Samsung", "model": "A52", "price": 25000}

# updating info
info.update({"color": "Black", "price": 24000})
print("updated dict =")
for i ,j in info.items():
    print(f"{i}  =  {j}")
#removing key model
print("model removed = ",info.pop("model"))

#final dictionary 
for i ,j in info.items():
    print(f"{i}  =  {j}")

#Q6

#creating  a dictionary 
dict3 = {'name': "tani" , 'age':18  , 'marks': 78, "weight": 65  , "height": 5.10}

print(dict3)

# use popitem  twice 
print(dict3.popitem())
print(dict3.popitem())

#clear the entire dictionary
dict3.clear()

#printing the final result
print(dict3)

# pop() - returns a value that is being removed 
# popitem() - returns key an value that  are being removed

#Q7

#create dict
d = {"a": 1, "b": 2}

#making copy of it
di= d.copy()

#Use setdefault() to add key "c" with value 3 (if it doesn't exist).
d.setdefault("c",3)

#Use setdefault() again for an existing key "a".
d.setdefault("a", 34)

print(f"original = ")
for i ,j in d.items():
    print(i , " = " , j)
print(f"copy = ")
for i ,j in di.items():
    print(i , " = " , j)


#Q8

# making keys
key= ["name", "age" , "weight"]

keys= dict.fromkeys(key, None)

# taking input
keys["name"] = input("Enter name = ")
keys ["age"] = int(input("Enter Age = "))
keys['weight'] = int(input("enter weight = "))

# printing the dict 
print("\n details = ")
for i,j in keys.items():
    print(i, " = ", j)

# cheak if any key exists 
a = input("\n Enter key = ")
if a in keys :
    print(f"{a} is present , {a} = {keys[a]}")


#Q9
con =[ "c1", "c2", "c3"]

#Store them in a dictionary with name as key.
key = dict.fromkeys(con,None)

#Take name, phone number, and email as input.
for i in con:
    name = input('enter name =')
    phone = int(input("Enter phone no. = "))
    email = input("Enter e- mail = ")
    key[i]={"name":name,"phone":phone, 'email':email}

search = input("\nEnter contact key to search (c1/c2/c3): ")

if key.get(search):
    print("contact found = ")
    print(f"name = {key[search]["name"]}")
    print(f"phone no.  = {key[search]["phone"]}")
    print(f"email = {key[search]["email"]}")


print(key.items())

#Q10

#creating an empty dictionary 
sms = {}

while True:
# taking input of every student from user 
    roll = int(input("Enter roll no. = "))
    
    if roll > 0 :

        name = input("enter name = ")
        age = int(input("Enter age = "))
        marks = int(input("enter marks = "))
# else condition to stop the input 
    else:
        break

# storing the student details in the dictionary
    sms[roll]= {"name" : name , "age":age , "marks":marks}

#creating the menu 
print( "Enter 1 - add student detail \n 2 - update marks of students\n 3 - search student by roll no. \n 4 - dispay all student data \n 5 - remove a studet  \n  0 - exit")

# doing operations on the bases of the menu 
while True :
    # asking for the task to perform 
    c = int(input("Enter choise = "))

    # performing the 1st operation 
    if c == 1 :
        # asking for the student roll no, to be added 
        rol = int(input("Enter roll no. = "))
        # cheaking if the roll no. is positive 
        if rol > 0 :
            # taking student details
            name = input("enter name = ")
            age = int(input("Enter age = "))
            marks = int(input("enter marks = "))
        # adding details of student into the dictionary 
        sms[rol]= {"name" : name , "age":age , "marks":marks}
    # condition to exit the menu     
    if c == 0 :
        break
    # performing the 2nd operation 
    if c == 2:
        #asking for student roll no 
        rol1 = int(input("Enter student roll no. = "))
        # updating marks of the student 
        if rol1 in sms.keys() :

            mks = int(input("Enter marks = "))
            sms[rol1]["marks"]= mks 

        # if the student dont exsist
        else:
            print("{rol1} is not present in the system") 

    # perforing the 3rd operation 
    if c == 3:
        # asking for roll no. 
        rol2 = int(input("enter roll  no. of the student = "))
        
        # cheaking if the roll no. exsists in the dictionry 
        if rol2 in sms.keys():
            # printing information of specif student 
            print(f"student iformation = \n {sms[rol2]}")
        # if enterd the wrong roll no. 
        else: 
            print(f"{rol2} roll no, dose not exist in the system !!")

    # performing the 4th operation 
    if c == 4 :
        # printing all the student data
        print("All student data : \n")

        # using for loop to print all student data neetly  
        for i , j in sms.items():
            print(f"\n student {i} = ")
            print(f"name = {"name"}")
            print(f"age = {"age"}")
            print(f"marks = {"marks"}")
    
    # performing 5th operation
    if c== 5 :
    # asing for the roll no. to be removed 
        rol3 = int(input("Enter roll no. to remove = "))
        
        # cheaking for the roll no in the dictionary 
        if rol3 in sms:
            # removing the data of student 
            sms.pop(rol3)
            print("Successfully remoed the student details ")
        else:
            print(f"{rol3} is not present in the system ")
