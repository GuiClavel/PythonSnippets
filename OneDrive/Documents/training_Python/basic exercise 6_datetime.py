# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old, except don’t explicitly write out the year. 
# Use the built-in Python datetime library to make the code you write work during every year, 
# not just the one we are currently in.

import datetime
askName=str(input('please enter your name: '))
askAge=int(input('please enter your age: '))
currentYear=(datetime.date.today())
yearforgoingto100=100-askAge
year100=currentYear.year+yearforgoingto100
print(year100)
