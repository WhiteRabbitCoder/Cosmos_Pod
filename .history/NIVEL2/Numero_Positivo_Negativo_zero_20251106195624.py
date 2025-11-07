#Creo la variable para que el usuario me ponga su numero
numero=int(input("Ingrese un Numero "))
#Aqui se usa el if para que si un numero es mayor al 0 marque que es positivo
if numero > 0:
    print("Su numero es positivo ")
#Aqui el elif se usa para verficar si el numero es menor al 0 que marque que es negativo
elif numero < 0:
    print("Su numero es Negativo ")
#Aqui se usa el else para que cuando el usuario ponga un numero
else:
    print("Su numero es 0")
