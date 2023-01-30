#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
#Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year)
#   https://www.practicepython.org/exercise/2014/01/29/01-character-input.html 


def age100(currentAge):
    agetotal=100-currentAge
    return agetotal

name=input('please indicate your name: ')

var_currentAge=input('now please indicate your age: ')
var_currentAge=int(var_currentAge)
var2_currentAge=str(age100(var_currentAge))

actualYear=2022
futureYear = actualYear + var_currentAge
futureYear_2=str(futureYear)

print("then you will turn 100 year's old in: "+var2_currentAge+" years, which means that it will be in the year "+futureYear_2)



