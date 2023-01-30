# Implement a listwise and function (returns true only if all the elements of the list are true). 
# Implement a listwise or function (returns true if at least one element is true).
# Examples:
# [False,True,False] → the or would return True.
#                       the and would return False.
# [True, True, True] → both would return True.
# [False, False, False] → both would return False.
# Hint: Think of the accumulator as an assumption of the result in both cases; the for is the attempt of the
# program to ‘disprove’ that assumption. Taking this into account, should the accumulator start as True or
# False? (Think about each case separately as the and/or don’t necessarily share the same initial value)

#USE AND OR

def listTrueFalse(x):
    # list01=[x]
    x=True
    if x==True and x!=False:
        print('True')
    else: print('False')
    print(x)

# userValue01=input('Please introduce a 1st value True or False: ')
# userValue02=input('Please introduce a 2nd value True or False: ')
# userValue03=input('Please introduce a 3rd value True or False: ')

# print(listTrueFalse(userValue01))