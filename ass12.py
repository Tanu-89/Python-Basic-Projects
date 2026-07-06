# Q1
 
# creating a function that counts vowels and returns the num of count 
def count_vowels(s):
    #putting all vowels in one set 
    vowels = {"a", "e","i","o","u",'A','E','I','O','U'}
    count = 0
    # running the for loop on the vowels
    for char in s:
        # increasig count of the vowels by one ever time there is a match 
        if char in vowels:
            count += 1
    # returning the final count of the vowels
    return count   

# taking input of vowels
s = input("enter word = ")
print("vowels count = ", count_vowels(s))



# Q2


# function analyze_string(s) that takes a string as input and
def analyze_string(s):

    #Prints its length using len().
    print("length of the strign = ", len(s))

    # Prints the string in reverse using slicing.
    print("reverse string = ", s[::-1])

    # Counts and prints how many vowels (a,e,i,o,u) are in the string (case insensitive).
    print("vowels = ", count_vowels(s))

    # Uses a for loop with range() to print each character with its positive and negative index.
    for i in range(len(s)):
        print(s[i], " index = " , i )

#Call this function with user input and handle empty string case.
while True :
    try :
        s= input("Enter string = ")
        if s=="":
            raise ValueError
        
    except ValueError:
        print("Empty string not allowed ")
    else:
        analyze_string(s)
        break



#Q3


# Create a function manage_marks() that:
def manage_marks():

    mark_list = []

    # Takes 5 subject marks as input from the user.
    while True:

        # Handles ValueError if non-numeric input is given.
        try:
            marks = int(input("Enter ur marks = "))
        except ValueError:
            print(" Enter only Numbers ")
        else:

            # Stores them in a list.
            mark_list.append(marks)

        if len(mark_list) == 5:
            break

        # Calculates and prints the average, highest, and lowest marks.
        
    print(mark_list)
manage_marks()