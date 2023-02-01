# Make a program that takes a date to the format ‘MM/DD/YYYY’. 
# Your program should determine whether the date is in the first half of the year (January-June) 
# or the second half (July-December). 
# Your output should be a sentence stating this.

var = (input("Please enter a date in this format: dd/mm/yyyy): "))
day,month, year = var.split('/')

if month==('01,02,03,04,05,06'):
    print(f"Your date (mm/dd/yyyy) is included within our January-June season: {month}/{day}/{year}")
else: print(f"Your date (mm/dd/yyyy) is included within our July-December season: {month}/{day}/{year}")

