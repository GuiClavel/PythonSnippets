#Implement an absolute value function (given a number it returns the absolute value)

#solution 1:
"""
def absolute(n):
    y=abs(n)
    return y
                      
print(absolute(-3))     #not working if an input is previously inserted though
"""
#solution 2:
def absolute2(n):
    number=int(n)
    if number<0:
        return number*(-1)
    else: return number
var=str(input('please indicate an integer n: '))
print(absolute2(var))