#Ask the user for a number. 
#Depending on whether the number is even or odd, print out an appropriate message to the user

displayNumber=int(input('please indicate an integer: '))
if displayNumber % 2==0:
    print("your number is even")
else: print("your number is odd")
