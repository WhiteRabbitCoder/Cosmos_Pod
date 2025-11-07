#Creo la variable de la edad para que el usuario la ingrese 
edad=int(input("Ingrese su edad "))
#Creo el if para saber si la edad del usuario es igual o mayor a 18 imprima que es mayor de edad
if edad >=18:
    print("Eres Mayor de edad")
#Creo el else para que si el usuario pone un numero menor a 18 marque inmediatamente que es mejor de edad
else:
    print("Eres menor de edad")
