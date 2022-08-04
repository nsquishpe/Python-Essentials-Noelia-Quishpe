# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 12:15:45 2022

@author: Laptop
"""

def isYearLeap (year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def daysInMonth(year, month):
    Meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    if month in Meses:
        if month == 4 or month == 6 or month == 9 or month == 11:
                return 30
        elif month == 2:
            #Febrero 29 dias
            if isYearLeap(year) == True:
                return 29
            #Febrero 28 dias
            else:
                return 28
        else:
                return 31
    else:
        return None
    
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")