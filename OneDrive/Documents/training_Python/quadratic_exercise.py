#A polynomial equation is written ax²+ bx+c = 0. 
# Make a function that given a,b and c solves the quadratic equation if there is(are) a real answer, 
# otherwise return False
#  inspiration:  https://www.geeksforgeeks.org/python-program-to-solve-quadratic-equation/

from math import sqrt


def quadratic(a,b,c):
    delta=b**(2)-4*a*c

    if delta>0:
        print(((-b)-(sqrt(b**(2)-4*a*c)))/(2*a))
        print(((-b)+(sqrt(b**(2)-4*a*c)))/(2*a))
    elif delta==0:
        print(-b/(2*a))
    else: print('no quadratic solutions here')


var_a=int(input('please enter an entire value for a (different than 0): '))
var_b=int(input('please enter an entire value for b: '))
var_c=int(input('please enter an entire value for c: '))
print(quadratic(var_a,var_b,var_c))
