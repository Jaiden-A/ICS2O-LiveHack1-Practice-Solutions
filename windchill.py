'''
-------------------------------------------------------------------------------
Name:		windchill.py
Purpose:	Write a program that gets the temperature(celsius) and wind speed (km/h)
then computes and outputs the windchill factor.

Author:	Fabroa.E

Created:	date in 04/12/2020
------------------------------------------------------------------------------
'''

print("****** Windchill Calculator ******")

# get temperature and windspeed
temp_c = float(input("Enter the temperature in celsius: "))
windspeed = float(input("Enter the windspeed (km/h): "))

# compute windchill
windchill = 13.12 + (0.6215*temp_c) - (11.37 * windspeed**0.16) + (0.3965 * temp_c * windspeed**0.16)

# output windchill
print("With the windchill factor, it feels like " + str(windchill) + "° outside.")


