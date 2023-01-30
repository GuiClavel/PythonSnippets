#Create a program that asks the user to enter their name and their age. 
#Print out a message addressed to them that tells  the year that they will turn 100 years old.

displayAge=int(input("please enter your age: "))   
age100=100-displayAge
currentYear=2022
year100=str(currentYear+age100)
displayFinal100=input("then you will turn 100 years old in "+year100)

