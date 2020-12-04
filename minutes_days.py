'''
-------------------------------------------------------------------------------
Name:		minutes_days.py
Purpose:	Write a program that lets you enter a number of minutes, and 
that will calculate the number of days, hours and minutes that represents 
(Hint: use the modulus operator).

Author:	Fabroa.E

Created:	date in 04/12/2020
------------------------------------------------------------------------------
'''
print("****** Minutes to Days and Hours ******")

# get number of minutes from user
minutes = int(input("Enter the number of minutes: "))

# compute days and hours
days = minutes//1440
remaining_minutes = minutes%1440
hours = remaining_minutes//60
final_minutes = remaining_minutes - hours*60

# output results
print(str(minutes) + " minutes is " + str(days) + " day(s) " + str(hours)+" hour(s) and " + str(final_minutes) + " minute(s).")

