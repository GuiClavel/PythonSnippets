import datetime

nameUser = input('write here your name: ')
ageUser = int(input('please write here your age: '))

thisYear = datetime.date.today()
birthUserYear = thisYear.year - ageUser 
year100 = birthUserYear + 100

print(f'congratulations {nameUser}, you will turn 100 in the year {year100}')
