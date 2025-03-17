'''
if en cascada:
estructura de control que permite
evaluar varias condiciones en 
cascada, es decir, si la primera
condicion no se cumple, 
se evalua la siguiente 
y asi sucesivamente 
'''

#ejemplo: 
# modificar el programa de votacion 
# para que considere la edad de 17 
# años 

edad = int(input("ingresa tu edad: "))
if edad > 18:      
      print ("puedes votar")
elif edad == 18:
    print ("bienvenido ciudadano, puedes votar con contraseña")
elif edad == 17:
    print ("puedes votar el proximo año")
elif edad < 9:
    print ("eres muy pequeño, tienes registro civil")
elif edad < 17:
    print ("eres muy joven aun, tienes tarjeta de identidad")
    print ("fin del programa")
      