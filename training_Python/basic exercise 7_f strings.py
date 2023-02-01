# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old), 
# except use f-strings instead of the + operator to print the resulting output message
import datetime
displayName=input('please enter your name: ')
displayAge=int(input('please enter your age: '))
convertedYear=100-displayAge                      #in how many years the user will turn 100
actualYear=datetime.date.today()                   #current date
mycurrentYear=actualYear.year                     #current year extracted
yearToWait=mycurrentYear+convertedYear          #which exact year in the future, the user will then turn 100
print(f'excellent {displayName}, you will then turn 100 in {yearToWait}')
