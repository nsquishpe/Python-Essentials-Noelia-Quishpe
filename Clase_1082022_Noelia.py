# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 18:55:15 2022

@author: Laptop
"""

def saludo2(nombre1, nombre2):
    print("Hola", nombre1)
    print("Hola", nombre2, "\n")

saludo2("Noelia", "Salome")
saludo2("Antonela", "Azucena")

def delivery(barrio, calle, casa):
    print("La dirección de la entrega de su pedido es: ", barrio, calle, casa)
    
barrio = input("Ingrese el barrio: ")
calle = input ("Ingrese el nombre de la calle: ")
casa = input ("Ingrese el número de casa: ")
delivery(barrio, calle, casa)

def resta(a,b):
    print(a-b)
resta(5,2)
resta(2,5)
resta(b=2, a=5)

#Suma
def suma(a,b):
    return a+b
#Resta
def resta(a,b):
    return a-b
#Multiplicacion
def multiplicacion(a,b):
    return a*b
#Division
def division(a,b):
    return a/b
#Potencia
def potencia(a,b):
    return a**b

opt=suma(5,4)
print(opt)

opt=resta(5,4)
print(opt)

opt=multiplicacion(5,4)
print(opt)

opt=division(5,4)
print(opt)

opt=potencia(5,4)
print(opt)


def lista(lis):
    for item in lis:
        print("Hola ", item, "\n")
        
lista(["Noe", "Mate", "Fer"])

def crealista(n):
    lista=[]
    for item in range(n):
        lista.append(item)
    return lista

crealista(4)



#Lambda   ANONIMAS
















