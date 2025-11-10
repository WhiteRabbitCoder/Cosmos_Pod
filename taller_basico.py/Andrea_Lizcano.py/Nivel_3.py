print("_________________Contar 1 al 10________________")

for i in range (11):
    print (i)



print("_________________Tabla de multiplicar________________")


Multiplicacion =int(input("Escoja cual tabla de multiplicar desea ver: "))
for i in range (1,11):
    resultado = Multiplicacion * i
    print (resultado)



print("_________________Contador regresivo con while________________")

Contador = 10  
while Contador >= 0:
    print (Contador)
    Contador -= 1 




print("_________________Adivina el número________________")

import random
numero_secreto = random.randint(1,5)
intento = 0 

while intento != numero_secreto:
    intento =int(input(f"adivina el numero 1-5 =>"))
    if intento < numero_secreto:
        print ("El numero secreto es mayor, buen intento")
    elif intento > numero_secreto:
        print ("El numero secreto es menor, buen intento")
    else:
        print ("Felicidades adivinaste")
print ("" 


)

while intento == numero_secreto:
    intento =int(input(f"adivina el numero 1-5 =>"))





print("_________________Sumar hasta que el usuario escriba 0________________")

n1 =(float(input("Por favor digite su primer numero a sumar(0 para terminar):" )))

Suma = 0 
while n1 != 0:
    suma = suma +  n1 
    n1  = float(input("Por favor digite el otro valor de la suma (0 para terminar )"))
    if n1 == 0: 
       print ("Suma finalizada")
       break 
print (f"El resultado de la suma es: ", {suma})








   





