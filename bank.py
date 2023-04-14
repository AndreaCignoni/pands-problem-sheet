# bank.py
# author : Andrea Cignoni
# weekly task2

# Prompting user to input two integers
number1 = int(input ('Enter amount1(in cent): '))
number2 = int(input ('Enter amount2(in cent): '))
# sum of the amounts
sum = (number1 + number2)
# the output concatenates a string and an integer in decimal format
print (f"The sum of this is €" + '{:.2f}'.format(sum/100.))
# In order to obtain the integer in the decimal format I have followed
# https://thepythonguru.com/python-string-formatting/