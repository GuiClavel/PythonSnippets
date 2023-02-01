# input and output

# def function and implemented it

# input function

# input income, country

# output citizenTax

""""
tax_rates={
    'colombia': 0.33,
    'switzerland': 0.2,
    'estonia': 0.2,
    'canada': 0.48
}

def citizenTax(income,country):
    country=tax_rates[country]
    calculus=income*country
    return calculus

income_user = input('enter the income here: ')
income_user=float(income_user)

country_user = input('enter the country here: ')

print(citizenTax(income_user,country_user))
"""

"""
def cashPayback(years,loan,rate):
    n = 12 * years       #  amount of monthly payments
    rate = (1+rate)**(1/12) - 1
    payback = (loan*rate) / (1 -(1+rate)**(-n))   # $$
    return payback, n      


print("Welcome to the program to calculate the payback of a loan!")

loan = input("Introduce the amount you were loaned: ")

loan = float(loan)

rate = input("Introduce the interests of the loan: ")

rate = float(rate)

years = input("Introduce the years to pay the loan: ")

years = int(years)

#years = 5

#loan= 20000

#rate = 0.1

print(cashPayback(years,loan,rate))
"""





"""
print("Welcome to the program to multiply a number by two!")

x = float(input("Please introduce your number: "))

print(x*2)
"""


def physics(time,v_0,h_0): 
    g = 9.8
    v = v_0 - g * time        
    h = -g/2 * time**2 + v_0 * time + h_0
    return v,h

print('here some physics for nerds')
v0 = input('please enter the v0 value: ')
v0=float(v0)

h0 = input('please now indicate a value for definying h0: ')
h0=float(h0)

time = input('finally we need to populate a value for the time t: ')
time=float(time)

print(physics(time,v0,h0))