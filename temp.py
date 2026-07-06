# Create a function manage_marks() that:
def manage_marks():

    # defining variables to be used further
    total = 0
    mark_list = []
    high , low = 0 , 100

    # Takes 5 subject marks as input from the user.
    while True:

        # Handles ValueError if non-numeric input is given.
        try:
            marks = int(input("Enter ur marks = "))
        except ValueError:
            print(" Enter only Numbers ")
        else:
            #storing total marks 
            total += marks


            # highest 
            if marks >= high :
                high = marks

            # lowest 
            if marks < low :
                low = marks

            # Stores them in a list.
            mark_list.append(marks)
        # takes only 5 inputs
        if len(mark_list) == 5:
            break

        # Calculates and prints the average, highest, and lowest marks.
    print(f"-- Highest marks = {high}")    
    print(f"-- Lowerst marks = {low}")
    print(f"-- Avg marks = {total//5}")
    print(mark_list)

manage_marks()


#Q4
