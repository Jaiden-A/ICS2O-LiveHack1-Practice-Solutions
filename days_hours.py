'''
-------------------------------------------------------------------------------
Name:		days_hours.py
Purpose:	Write a program that lets you enter a number of hours, and that converts 
it to days and hours. For example, 111 hours = 4 days and 15 hours. 
(Hint: use the modulus operator).

Author:	Fabroa.E

Created:	date in 04/12/2020
------------------------------------------------------------------------------
'''
print("****** Hours to Days and Hours ******")

# get number of hours from user
hours = int(input("Enter the number of hours: "))

# compute days and hours
days = hours//24
remaining_hours = hours%24

# output results
print(str(hours) + " hours = " + str(days) + " days and " + str(remaining_hours)+" hours.")

