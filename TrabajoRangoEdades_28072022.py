# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:31:32 2022

@author: Laptop
"""

dato1 = input("Ingrese su nombre: ")
dato2 = input("Ingrese su apellido: ")
dato3 = input("Ingrese su ubicación: ")
dato4 = int(input("Ingrese su edad: "))

#Crear 4 rangos minimos.

if dato4>= 0 and dato4<= 5:
    print("Primera Infancia")
elif dato4>= 6 and dato4<= 11:
    print("Infancia")
elif dato4>= 12 and dato4<= 17:
    print("Adolescencia")
elif dato4>= 18 and dato4<= 26:
    print("Juventud")
elif dato4>=27 and dato4<= 59:
    print("Adultez")
else:
    print("Persona mayor")