#For this exercise, we will keep track of when our friend’s birthdays are, 
# and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, and return the birthday of that person back to them. 

birthdayFriends={
    "gui":1985,
    "amalia":1986
}
displayName=input('please indicate your friend name: ').lower
if displayName=='amalia':
    print(birthdayFriends["amalia"])
else: print(birthdayFriends["gui"])



# other way to code: 
#  
# birthday_diccionary = {
#         'Gui': '25/6/85',
#         'Amalia': "1/7/86",
# }

# nameBirthday = input('please enter the name of the birthday person to celebrate: ')
# if nameBirthday == 'Gui':
#         print(birthday_diccionary['Gui'])
# else: print(birthday_diccionary['Gui'])
