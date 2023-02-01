
askUser = int(input('please enter a number of your choice: '))

myList = range(1,101)
mySecondList = []

for element in myList:
 if askUser % element == 0:
    mySecondList.append(element)
print(mySecondList)