#Implement a function that takes as input three variables, and returns the largest of the three. 
#Do this without using the Python max() function!

displayNumber1=int(input("please enter a 1st integer number: "))
displayNumber2=int(input("please enter a 2nd integer number: "))
if displayNumber1<displayNumber2:
    print('number 2 is bigger')
else: print('number 1 is bigger')

displayNumber3=int(input("please enter a 3rd integer number: "))
if displayNumber2<displayNumber3:
    print('number 3 is bigger')
else: print('number 2 is bigger')
