'''
Estructura de control if:
se utiliza para tomar decisiones 
basadas en expresiones condicionales
'''
#ejem 1: if simples
edad = int (input("ingrese tu edad:  "))
documento = input ("tienes documento? (si/no):  ")
#condicional: si es la edad es mayor o igual a 18
if edad >= 18 and documento =='si':
        #codigo patra cuando es mayor a 18
    print("eres mayor de edad y tienes documento, puedes votar")
else:
    #codigo para cuendo es menor a 18
     print("eres menor de edad o no tienes documento, no puedes votar")
    #codigo que se ejecuta siempre
     print("fin del programa")