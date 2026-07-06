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


