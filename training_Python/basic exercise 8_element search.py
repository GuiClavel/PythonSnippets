# Write a function that takes an ordered list of numbers 
# (a list where the elements are in order from smallest to largest) and another number. 
# The function decides whether or not the given number is inside the list and returns 
# (then prints) an appropriate boolean.

a=[1,2,3,4]
b=int(input('please enter an integer number: '))
ok=True
notOK=False
if b in a:
    print(ok)
else: print(notOK)

