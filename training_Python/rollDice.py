import random as rand

# randint(a,b) -> returns a number between a,b including both

# def funct(a,b):
#     return rand.randint(a,b)
# display=int(input('enter a value for A (integer): '))
# display_B=int(input('enter a value for B (integer): '))
# print(funct(display,display_B))

# you'll generate a random number between 1 and 6
# the user has to guess it
# if they do they win, if they don't they lose


continue_var=True


while continue_var:
    var=rand.randint(1,6)

    display_user=int(input('give me the correct number: '))

    if display_user != var: 
        print('you failed')
    elif display_user == var:
        print('you succeeded the 1st time')
        continue_var=False

# var_random_number=rand.randint(1,6)
# display_user=int(input('guess a number: '))
# display_user2=(input('do you want to play again (y/n): '))
# def play_game():
#     if int(display_user)!= var_random_number:
#           print ("You Lose!")
#     else:
#           print ("You Win!")

# def play_again():
#     return display_user2.lower() == "y"

# while True:
#     play_game()
#     if not play_again(): break

# print ("OK Goodbye")



