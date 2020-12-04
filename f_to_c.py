'''
-------------------------------------------------------------------------------
Name:		f_to_c.py
Purpose:	Write a program that lets you enter a degree measure in Fahrenheit 
and prints the result in celsius degree measure.

Author:	Fabroa.E

Created:	date in 04/12/2020
------------------------------------------------------------------------------
'''

print("****** Fahrenheit to Celsius Converter ******")

# get Fahrenheit from user
temp_f = float(input("Enter the temperature in Fahrenheit: "))

# compute celsius
temp_c = (5/9) * (temp_f-32)  

# output celsius
print("The temperature in Celsius is " + str(temp_c) + "°.")

