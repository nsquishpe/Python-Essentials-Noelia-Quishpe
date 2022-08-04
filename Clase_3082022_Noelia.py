# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 19:51:24 2022

@author: Laptop
"""

try:
    print("1")
    x=1/0
    print(2)
except:
    print("Something went wrong")
print("3")


try:
    x=int(input("Enter a number:"))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry")
except ValueError:
    print("You must enter an integer value")
except:
    print("Oh dear, something went wrong")
print("end....")


try:
    y=1/0
except ArithmeticError:
    print("Error")
except ZeroDivisionError:
    print("ggg")
    
try:
    y=1/0
except ZeroDivisionError:
    print("ggg")     
except ArithmeticError:
    print("Error")
   