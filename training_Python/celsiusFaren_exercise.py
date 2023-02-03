#Make a program that takes the temperature in celsius and outputs the temperature to farenheit. 
# Make sure that your ouput is a sentence and not just the number.

celsius = int(input('please provide a temperature in Celsius: '))    
F = celsius * (9/5) + 32    # F = C * 9/ 5 + 32
F_str=str(F)
print("then the temp. in Faren. is equal to "+F_str)