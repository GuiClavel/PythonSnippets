import datetime

#list end
a_list = [10,12,62,101]
b_list = a_list[1],a_list[2]

#1st game step: 
FirstNumberUser = int(input('Welcome to this mini game! For beginning please indicate a number: '))
if FirstNumberUser >= a_list[0] and FirstNumberUser <= a_list[3]:
    print('well done, you passed the 1st step: +1 point')             # +1 pt.
else: print('sorry, you missed this step, but keep playing')

# #2nd game step: 
secondNumberUser = int(input('harder now, please indicate another number for a tiny range: '))
if secondNumberUser >= b_list[0] and secondNumberUser <= b_list[1]:
    print('well done!! you passed this 2nd step: +1 point')             # +1 pt.
else: print('sorry, you missed this step, but keep playing as you\'ll have other opportunities')

#birthday dictionary
nameUser = input('now please tell us a bit about yourself, what is your name: ')
ageUser = int(input('thanks, and how old are you: '))
hobby = input('perfect! For finishing, just tell us your most preferred hobby: ')

userAgeDictionary = {
    'nameUser':2,
    'ageUser':3,
    'hobby':1
}

#3rd game step: guessing ranking of previous answers  (+max of three numbers)
thirdNumberUser = int(input('Ok. Now, between 1 to 3 included, which number do you think we assigned to your answer regarding your age: '))
if thirdNumberUser == 3:
    print('you\'re level super master! Good answer')
else: print('not this value, but no problem, let\'s keep playing!')

if userAgeDictionary['ageUser'] > userAgeDictionary['nameUser'] and userAgeDictionary['ageUser'] > userAgeDictionary['hobby']:
    print('interesting, so now just to tell you that we will use your age as top priority for a next calculation')
else: print('we will do nothing else, let\'s go back home')

#calculation of birth year
thisYear = datetime.date.today()
yearBirthUser = thisYear.year - ageUser

#odd or even (with a f string)
if yearBirthUser % 2 == 0 :
    print(f'Fantastic {nameUser,} you were then born in {yearBirthUser} which is an even year ;) Thanks for having played!')
else: print(f'Looks great, thanks {nameUser}: you were then born in {yearBirthUser} which is an odd year :) Thanks for having played!')