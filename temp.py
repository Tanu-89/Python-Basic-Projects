# function analyze_string(s) that takes a string as input and
def analyze_string(s):

    #Prints its length using len().
    print("length of the strign = ", len(s))

    # Prints the string in reverse using slicing.
    print("reverse string = ", s[-1])

    # Counts and prints how many vowels (a,e,i,o,u) are in the string (case insensitive).
    print("vowels = ", count_vowels(s))

    # Uses a for loop with range() to print each character with its positive and negative index.
    for i in range(len(s)):
        print(s[i], " index = " , i )

s= input()
analyze_string(s)