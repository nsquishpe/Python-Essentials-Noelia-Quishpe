# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 18:06:30 2022

@author: Laptop
"""

lista = ["R1",5,5.67,True]
print(type(lista))

tupla = ("R1",5,5.67,True)
print(type(tupla))

print(lista[0])
print(tupla[0])

print(lista[-1])
print(tupla[-1])

#Modificar lista
lista[3]=False
print(lista)

#Eliminar posicion 4 de la lista
del lista[3]
print(lista)

#Diccionarios
dict1 = {False:"Valor de estado",
         5001: "Noelia Salome",
         "R1":"10.10.10.1"}

print(dict1)
print(dict1['R1'])

#Agregar un valor a un diccionario
dict1["R2"]="10.10.10.2"
print(dict1)

#Consulta, busca P1 en diccionario
print('R1' in dict1)





























