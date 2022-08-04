# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 20:07:52 2022

@author: Laptop
"""

def Fibonacci(n):
    if n <= 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
    
    
def suc_fib(n):
    for i in range(n-1):
        print(Fibonacci(i))
        
suc_fib(8)
suc_fib(20)


