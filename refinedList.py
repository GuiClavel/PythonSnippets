
myList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
mySecondList = []

for element in myList:
    if element < 5:
        mySecondList.append(element)
    else: print('not ok')

print(mySecondList)