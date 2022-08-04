# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 18:08:34 2022

@author: Laptop
"""

#Estructura repetitiva for
for item in range(10,0,-1):
    print(item)
    
#Imprimir elementos de una lista
lista = ["R1","R2","R3","R4","S1","S2","S3"]
for item in lista:
    print(item, end=" ")
    
for i in range(1,len(lista)):
    print(i)
    
lista1 = []

for item in lista:
    if "R" in item:
        lista1.append(item)
print(lista1)

lista = ["R1","R2","R3","R4","S1","S2","S3"]

lista1 = []
lista2 = []

for item in lista:
    if "R" in item:
        lista1.append(item)
    else:
        lista2.append(item)
print(lista1)
print(lista2)


#Bucle while

contar = 5
contador = 1
while(contador <= contar):
    print(contador, end=" ")
    contador += 1



contar = 5
contador = 1
while(True):
    print(contador, end=" ")
    contador += 1
    if contador >  contar:
        break











