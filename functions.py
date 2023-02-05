#Write a function calculate_square that takes a single argument x and returns the square of x

def calculate_square(x):
    elem = x * x
    return elem
print(calculate_square(2))

#Write a function calculate_average that takes a list of numbers as an argument 
#and returns the average of the numbers

# myList = []
def calculate_average(myList):
    avg = sum(myList) / len(myList)
    return avg
print(calculate_average([1,3,5,9,11]))

#Write a function is_even that takes a single argument x 
# and returns True if x is even, and False otherwise.
x = None
def is_even(x):
    if x % 2 == 0:
        return True
    else: return False
print(is_even(5))