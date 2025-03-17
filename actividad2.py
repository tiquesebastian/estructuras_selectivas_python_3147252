'''
elabore un programa en python que determine si usted puede:
a) casarse
b)comprometerse
c)quedarse soltero
con base a las siguientes caracteristicas (variables):
- estado civil (string)
"soltero", "casado" y "comprometido")
edad (int)
temperamento (string= 
"buena persona" , "mala persona")
-fisico (string = lindo/a, feo/a)
'''
estado_civil = input ("ingrsa tu estado civil: (soltero/casado/comprometido)")
edad = int (input ("ingresa tu edad: "))
temperamento = input ("ingresa tu temperamento: (buena persona/mala persona)") 
fisico = input ("ingresa tu fisico: (limdo/a , feo/a)")
salario = int (input("ingresa tu salario"))
if estado_civil == "casado" or estado_civil == "comprometido" : 
    print ("no puedes casarte con esa persona, por que ya tiene compromiso puto ")
    

elif edad < 18 :
    print ("no puedes acercarte a esa persona por que no tiene la edad suficuiente")
    
elif temperamento  == "mala persona":
    print ("no puedes acercarte a esa persona por que te generaria estres")
    
    
elif fisico == "feo":
    print ("no puedes acercarte a esa persona por que no te atrae fisicamente")
    
        
elif salario > 2000000:
    print ("no puedes acercarte a esa persona por que es pobre")
    

else :
    print ("puedes acercarte a esa persona ")
    print ("fin del programa")