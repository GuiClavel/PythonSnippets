#Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?
#   https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html 

def define_number(listNumbers):
    n = len(listNumbers)
    median_even=((n/2)+((n-1)/2))/2
    median_odd=(n-1)/2

varNumber=input('please enter in here a positive integer: ')
varNumber=int(varNumber)

if varNumber % 2 == 0:
    print('your selection is an even number')
else: print('your selection is an odd number')