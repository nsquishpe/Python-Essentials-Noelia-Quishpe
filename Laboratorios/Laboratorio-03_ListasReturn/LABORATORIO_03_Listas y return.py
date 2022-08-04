# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:07:03 2022

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

def daysInMonth (year, month):
    Meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #Valida meses coherentes
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

def dayOfYear(year, month, day):
    if day>=1 or day<=31:
        if(day<=30 and daysInMonth(year, month)== 30):
            return 30
        elif(month == 2):
            #Febrero 29 dias
            if (day<=29 and daysInMonth(year, month) == 29):
                return 29
            #Febrero 28 dias
            elif(day<=28 and daysInMonth(year, month) == 28):
                return 28
            else:
                None
        elif(day<=31 and daysInMonth(year, month)== 31):
            return 31
        else:
            None
    else:
        None
        
        
print(dayOfYear(2000, 11, 24))
print(dayOfYear(2001, 2, 31))
print(dayOfYear(2016, 2, 29)) #Bisiesto
print(dayOfYear(2001, 12, 31))
print(dayOfYear(2000, 12, 31))