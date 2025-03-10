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
#ejemplo 4: jerarquia de operadores 
y = False and not True or False
print ("el resultado de operar jerarquia de operadores es", y)

#ejemplo 5: operadores relacionales y logicos 
y= not 3>4 and 4==4 or 3<2

#ejemplo 6: operadores aritmetricos,
#relacionales y logicos

y = 3 + 5 * 2 > 3 and 4 == 4 or 3 < 2

print ("el resultado de ooperadores aritmetricos es", y)


#ejemplo 7: con parentesis
y = (3 + 5) * (2 > 3)and 4 == 4 or not 3 < 2
print ("el resultado con parentesis es", y)


#ejemplo 8: todo junto
y = 4** 2 * 3 < 6 / (7-5) and 7 * 2 + 1 == 14 or not 3 + 5 < 2
print ("el resultado es:", y)
