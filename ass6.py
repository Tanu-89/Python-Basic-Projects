#Q1

#list with 5 int elements
l1= [ 3, 5, 7, 4, 8]
print(f"\n list with 5 elements = {l1}")

# creating empty list 
'''using list function '''
l2= list()
print(f"\n empty list created using function = {l2}")
'''using [] '''
l3= []
print(f"\n empty list reated using [] = {l3}")

# list with mix data type
l4 = [5 , 6.9 , "samu", True]
print(f"\n list with multiple datatypes = {l4}")

# list of 7 zeros using repetation 
l5 = [0]
print(f"\n printing the list with 7 zeros using repetation = {l5*7}\n ")


#Q2

#creating list fruits
fruits = ["apple", "banana", "mango", "orange", "grape"]

#printing 1st element 
print(f"\n 1st elemtent of list = {fruits[0]}")

#printing third item 
print(f"\n 3rd item of list = {fruits[2]}")

# printing the last item of list 
print(f"\n last item of list = {fruits[-1]}")

#printing the 2nd last item of list 
print(f"\n 2nd last item of list = {fruits[-2]}")

a = int(input("\n Enter number from 0-4 = "))
if a < 5 :    
    print( f"\n list element at {a} = {fruits[a]}")
else:
    print(" invalid input !!")


#Q3

#making a list
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#first 4 elements
print(f" first 4 elements of list = {numbers[:4]}")
#last three elemnts 
print(f" last 3 elements of list = {numbers[-3:]}")
#elements from index 2-7
print(f" last 3 elements of list = {numbers[2:8]}")
#element at every 2 index 
print(f" last 3 elements of list = {numbers[::2]}")
#list in reverse order 
print(f" last 3 elements of list = {numbers.reverse()}")


#Q4

#creating list 
colors = ["red", "blue", "green", "yellow"]
print(colors)

#removing blue
colors.remove("blue")
print(colors)

#inserting purple where blue was
colors.insert(1,"purple")
print(colors)

#appending black in the last
colors.append("black")
print(colors)

#Q5

#creating empty list 
list2= []

#appending 5 cities name 
list2.append("Pune")
list2.append("Mumbai")
list2.append("Chennai")
for i in range(2):
    a=input("\n enter city name = ")
    list2.append(a)

#adding wakanda at 2nd positiion 
list2.insert(1, "Wakanda")

# printing list 
print(f"\n final list = {list2}")


#Q6

#creating list
items = [10, 20, 30, 20, 40, 50]

#removing the first 20 ffrom the list 
items.remove(20)
print(f'\n First occurance of 20 removed : {items}')

#Remove the item at index 3 using pop() and print the removed value.
print(f"\n Item at 3rd position = {items[3]}")
items.pop(3)
print(f"\n After removing the 3rd item = {items}")

#Remove the last item using pop().
items.pop(-1)
print(f"\n Removed the last item = {items}")

#Clear the entire list using clear().
items.clear()
print(f"\n Cleared the list = {items}")


#Q7

#create a list 
scores = [85, 92, 78, 92, 65, 92, 88]
print(scores)
#finding the index of the 1st ocurance of 92
print(f"\n Index of the 1st ocurance of 92 = {scores.index(92)}")
#coutnign the occuracnce of the no. 92
print(f"\n No. 92 has occured {scores.count(92)} times ")
#taking no. from user to check if its in the list 
a1=int(input("enter a number = "))
if a1 in scores:
    print(f"\n {a1} is present in list at {scores.index(a1)} index and has occured {scores.count(a1)} times")
else:
    print(a1, " dosent exist in the list !!")


#Q8


#creaing list 
marks = [45, 78, 65, 90, 34, 82, 71]

# printing the list in ascending order 
print(f"\n ascending order of the list = {marks.sort()}")
# printing the list in descending order 
print(f"\n descending order of the list = {marks.sort(reverse=True)}")
#reversing the original list 
print(f"\n reverse list = {marks.reverse()}")


#Q9


# creating lists 
list1 = [1, 2, 3]
list3 = [4, 5, 6]

# Using extend() to add list2 to list1.
list1.extend(list3)
print(f"\n extend () ={ list1}")
# Using append() to add list2 to a copy of list1.
list1.append(list3)
print(f"\n append () ={ list1}")

# append adds a new list to the existing list 
# whereas extend merges both of the lists


#Q10


#creating a list for Student Marks Manager
smm = []

# taking subjes marks  as input
print("enter marks for 5 subjects on by one out of 100 \n")
for i in range(5):
    a2= int(input("Enter marks = "))
    smm.append(a2)
print(f"\n marks = {smm}")

# adding another subject marks 
smm.append(84)
print(smm)

# sorting marks in descending order 
print(f"\n marks in Descending order = {smm.sort(reverse=True)}")

#printing the avg marks 
avg=0
for i in smm:
    avg+=i
avg_mks= avg//len(smm)
print(f"\n Average marks = {avg_mks}")

# Use len() to show total number of subjects.
subjects = len(smm)
print(f'\n total no. of subjests are {subjects}')

