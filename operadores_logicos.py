'''
operadores logicos 

aquellos que operan unicamente 
con valores booleanos (V F)
acorde a las tablas de verdad 

'''

#ejemplo 1: operador not 
y = not True 
print("el resultado de operar con not es", y)

#ejemplo 2: operador and 
y= False and True 
print("el resultado de operar con and es", y)

#ejemplo 3: operador or 
y = False or False
print ("el resultado de operar con and es", y)

'''
jerarquia operadores 
(logicos inclusive)
1. ()
2. **
3. *,/,%,
4. +,-
5. <, >, <=, >=, ==,!=
6. not
7. and
8. or  

'''
y = False and not True or False
print ("el resultado de operar jerarquia de operadores es", y)
