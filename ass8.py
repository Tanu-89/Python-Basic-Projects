#Q!

#set of 5 integers 
st1= { 2, 5, 6, 7, 8 }
print(f"\nset of 5 intergers = { st1}")
print(f"\ntype={type(st1)}")

#set with mixed data types
st2={ 2, 5.5 , "tanu"}
print(f"\nmixed datatyped set = {st2}")
print(f"\ntype={type(st2)}")

#creating the empty set 
st3= set()
print(f"\nempty set = {st3}")
print(f"\ntype={type(st3)}")

#string set using the consstrutor
st4= set("Hello")
print(f"\nset using constructor = {st4}")
print(f"\ntype={type(st4)}")


#Q2
 
#creating set 
numbers = {10, 20, 30, 20, 40, 10, 50}

#printing the set multiple times

print(f"\nset = {numbers}")
print(f"\nset = {numbers}")
print(f"\nset = {numbers}")
print(f"\nset = {numbers}")

# using the indexing 
#    print(numbers[0])
""" TypeError: 'set' object is not subscriptable 
    set dont have any fixed index of any element , therefore it is not ordered , 
    and thats why we cant use indxing or slicing on a set 
"""

#Q3

#creating an empty set 
color= set()

#taking the elements of color from user 
for i in range (5):
    c = input("Enter color name = ")
    color.add(c)

#printing the set
print(color )

#taking input from user 
co= input("Enter color name= ")

if co in color:
    print(f"{co } is  in {color}")
elif co not in color:
    print(f"{co} is not in {color}")
else:
    print("Invalid input!!")


#Q4


#creating the set 
fruits = {'apple', 'banana', 'mango'}
print(f"fruits = {fruits }")
#  adding orange 
fruits.add("Orange")
print(f"fruits = {fruits }")

#  adding banana 
fruits.add("Banana")
print(f"fruits = {fruits}")

#removing mango 
fruits.remove("mango")
print(f"fruits = {fruits}")

# discarding grape
fruits.discard("grape")
print(f"fruits = {fruits}")


#Q5


#creating set
s = {100, 200, 300, 400, 500}

#using pop to remove one item to print
print(s.pop(100))

#printing the set
print(f"set after pop = {s}")

#clearing the list 
s.clear()

#printing the cleared list
print(s)

''' 
    remove() - removes searches the element in the set to remove it , but if the element 
    is absent in the set , the it throws error 

    discard() - discard removes the element from the set dirctly and it dont throw any 
    error if the element is absent in the set 

    pop() -    pop removes the element and returns which element has been removed

'''

#Q6

#creating sets
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

#creating the copy of set1 
copyset= set1.copy()

print(f"copy set = {copyset}")

#Update set1 with elements from set2 using update().
set1.update(set2)

# printing the sets
print(f"\n Original set ={ copyset}")
print(f"\n updated set = {set1}")


#Q7


#creating set 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# printing the union of set a and set b 
''' it mixes both the set and removes the duplications and returns a set with both set  elements  '''
# union()
print(f"union of A and B = {A.union(B)}")

# | operator
print(f" \n union of A and B = {A|B}")

#Print the intersection of A and B
""" it returns a set which has the comman elements of both lists """
# using intersection()
print( f"\n Intersection of A , B = {A.intersection(B)}")

# using the & operator
print(f"\n Intersectio of A , B ={A & B}")



#Q8


#creating an empty set
num = set()

# taking multiple input from user
print("enter 6 non repeating numbers")
for i in range(6):
    a1= int(input("\n Enter the number = "))
    num.add(a1)

print(num)

3
# adding more numbers using add
num.add(50)
num.add(40)

print(num)

# removing  one number
num.discard(30)
print(f"set after discard = {num}")

#printing the final set 
print(f" \n final set = {num}")


#Q9

#list
scores = [85, 92, 78, 92, 85, 88, 95, 78]
print(scores)

# converting list to set
unique_scores= set(scores)

#printing unique scores
print(unique_scores)

#converting the set back to the list and then sorting it 
list1= list(unique_scores)
print(f" sorted list = {list1.sort()}")

#printing the total number of unique scores
print(f"total number of unique scores = {unique_scores.len()}")



#Q10 Unique Item Collector program

uic = set()

# taking input from user 

#   puttin conditions on the input 
print(" \n Enter any items , if you dont want to add number please enter : -1 ")
print(" \n If you dont want to enter string then enter : sss ")
print(" \n If you want to stop entering the items the enter both -1 and sss ")

#   taking mutiple inputs in the runtime 
while True:

    a = input("\n Enter a string = ")
    b = int(input("\n Enter a number = "))
    #   condition to break the input loop
    if a == "sss" and b == -1:
        break
    else:
        #   adding inputs to set
        if  a != "sss":
            uic.add(a)
        if b != -1:
            uic.add(b)

# printing all the inputs stored in set
print(f"\n {uic}")


# creating an menu 
# making the menu appear multiple times 
while True:
    print("\n 1. add item = 1 \n 2. remove item = 2 \n 3. show all unique item = 3 \n  4. Check if an item exists = 4 \n 5. clear all items = 5 \n 6. exit = 0 ")
    choise = int(input("Enter ur choise = "))

    #   performing the task of adding item to set  
    if choise == 1:
        #   asking for wether to add string or integer
        print("\n choose either number or string : \n number = 21 \n string = 31 ")
        choise2 = int(input("\n enter the choise = "))

        #   adding an interger to the set
        if choise2 == 21:
            number = int(input("\n enter number = "))
            uic.add(number)
            print(f"\n number added = {uic}")

        #   adding string item to the set 
        elif choise2 == 21:
            item = input("\n Enter the item = ")
            uic.add(item )
            print(f"\n item added = {uic}")

        #   error handling 
        else:
            print("\n Invalid Input !! ")

    #   performing the task of removing an item 
    elif choise == 2 :
        #   asking if the item to be removed is number or string 
        print("\n choose either to remove number of an item :\n number = 21 \n string = 31 ")
        choise3 = int(input("\n Enter your choise :"))

        #   removing an number from the set
        if choise3 == 21:
            numr= int(input("\n Enter number to remove = "))
            uic.discard(numr)
            print(f"\n number removed = {uic}")

        #   removing an string item from the set
        elif choise3 == 31:
            strr= input("\n Enter the item to remove = ")
            uic.discard(strr)
            print(f"\n Item remmoved = {uic}")

        #   to handle wrong input
        else:
            print("\n Invalid Input !! ")

    #   performing the task of printing the set 
    elif choise == 3:
        print(" \n All unique items = ") 
        print(uic)

    #   performing the task of finding the item is present in the set or not
    elif choise == 4:  
    #   asking user if the item is number or string 
        print("\n is the item number or string , if yes then u know the drill \n number = 21 \n string = 31")
        choise4 = int(input("\n Enter your choise = "))

        if choise4 == 21:
        #   taking the inputof the number to check 
            numchk= int(input("\n Enter the number to check = "))

            if numchk in uic:
            #   cheaking if the number is in the set
                print(f"\n {numchk} is present in the set ")
                print(uic)

            else:
            #   if the number is not in the set 
                print("\n it is not present in the set")
        elif numchk == 31:
        #   taking the input of the string  to check 
            strchk= input("\n Enter the item to check = ")

            if strchk in uic :
            #   checks if the string is in the set
                print(f"\n {strchk} is present in the set \n")
                print(uic)

            else:
            #    if the strin is not in the set
                print("\n it is not present in the set ")

    #   performing the task of clearing the set 
    elif choise == 5 :
    #   making sure if the user wants to clear the set 
        yn= input("\n Are you sure you want to clear the set yes/no = ")

        if yn =="yes":
        #   clearing the set as user wants 
            uic.clear()
            print(f"\n set cleared = {uic}")

        elif yn == "no":
        #   user dont want to clear the set 
            print("\n",uic)

        else:
        #   error handling 
            print("\n Invalid input !! ")

    #   existing the loop and menu 
    elif choise==0:
        print("\n Program ended !#")
        break 
