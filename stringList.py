#Ask the user for a string and print out whether this string is a palindrome or not. 
#ps: a palindrome is a string that reads the same forwards and backwards.

def palindrome(word):
    return word == word[::-1]

askUser = input("Enter a string: ")
if palindrome(askUser):
    print(f"{askUser} is a palindrome")
else:
    print(f"{askUser} is not a palindrome")