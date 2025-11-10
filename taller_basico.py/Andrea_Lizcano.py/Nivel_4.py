print("_________________Lista de frutas.________________")

Frutas = ["frambuesa", "mango", "piña", "sandia", "naranja", "uchuva", "curuva", "mamon", "manzana"]

for fruta in Frutas:        # La funcion recorre e imprime cada fruta 
     print (fruta)
Frutas.remove("uchuva")    # La funcion remove cumple con eliminar cualquier elemento de la lists 
print (Frutas)

buscar_fruta = input("Ingrese la fruta que desea buscar en la lista: ")
if buscar_fruta in Frutas:    #Se utiliza para buscar un elemento que se encuentre en la lista 
     print (f"{buscar_fruta}, Se encuentra en la lista. ")
else:
   print(f"{buscar_fruta}, no se encuentra en la lista.")








print("_________________Lista de números y promedio.________________")

Numeros= [11,2,31,14,5]
for numero in Numeros:
    print (numero)
    suma  = sum(Numeros)              #Se realiza una suma de los numeros que se encuentran en lista
print ("La suma total de los numeros en lista son:", suma)

Promedio = sum(Numeros) / len(Numeros)
print ((f"El promedio de los numeros es: "), {Promedio})





print("_________________Números pares________________") 

numeros = [1,2,3,4,5,6,7,8,9,10,]
pares =[]                             # La variable donde guardaremos solo los pares 

for numero in numeros:
    if numero % 2 == 0:
       pares.append(numero)         #Agrega a la variable que creamos anteriormente los numeros pares

print(f"Números pares: {pares}")


print("_________________Números repetidos________________") 

numeros = [1,2,3,5,6,4,3,1,3,4,9,7,4,2,4,6,3,6,9,7,8]
numeros_unicos =[]

for numero in numeros:
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)  #Agrega los numeros por unidad, sin repetir 
print(f"Números únicos (sin duplicados): {numeros_unicos}")

