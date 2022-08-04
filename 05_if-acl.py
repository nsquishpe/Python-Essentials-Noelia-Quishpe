# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:21:14 2022

@author: Laptop
"""

acl = int(input("Ingrese el # de ACL: "))
if acl >= 1 and acl <= 99:
    print("la ACL es estandar")
elif acl >= 100 and acl <= 199:
    print("la ACL es extendida")
else:
    print("El # ingresado no es de una ACL")