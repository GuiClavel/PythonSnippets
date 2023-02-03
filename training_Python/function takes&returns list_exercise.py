# make a function that takes in a list of numbers and a number k, 
# and returns a list with only the elements greater or equal than k.
# example:
# [1,11,7,2,5,1], 5 → [11,7,5]

list01=[1,11,7,2,5,1]
k=5
list01.append(k)

var=[k for k in list01 if k >= 5]       #list comprehension
print(var)