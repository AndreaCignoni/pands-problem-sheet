# Collatz.py
# The user is asked to input any positive integer
# and the number given will be devided by two if even
# or, if odd, multiplied by three and added of one.
# This calculation will be repeated until the result will be equal to one
# Author: Andrea Cignoni

# requesting user to input a number
n = int(input('Please enter a positive integer: '))
def collatz(n):
    # an empty list is taken to store all sequence values
    lst=[]
    lst.append(n)
    # While loop is used to check if the condition is equal to one
    while(n != 1):
        # If the number is not equal to one the number is checked to see if it is even or odd
        if(n %2==0):
            n=n//2
            lst.append(n)
        # If the result gives an odd number then the amount is multiplies by 3 and one is added
        else:
            n = n * 3 + 1
            # All the values are appended to the list
            lst.append(n)
    print (*lst)
# The list is the Collatz sequence of the given number
collatz(n)