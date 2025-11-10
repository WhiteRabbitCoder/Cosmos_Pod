#print("_________________Mayor_Edad________________")

#Edad= int(input("Ingrese por favor su edad actual: "))
#if Edad >=21:
 #   print ("Usted es mayor de edad.")
#else:
#    print ("Usted es menor de edad.")



#print("_________________Numero_Positivo/Negativo_0________________")

#Numero = int(input("Por favor ingrese el numero a identificar: "))
 
#if Numero >= 0:
#    print("Es un numero positivo")

#elif Numero==0:
#    print("El numero es cero")

#else :
#    print("El numero es negativo")
    



#print("_________________Par/Impar________________")

#for i in range (0,10,2): 
#    print (f"Los numero pares son:", {i})
    
#for i in range (1,10,2):
#     print  (f"Los numeros impares son:", {i})
     


#print("_________________Calculadora_Basica________________")

#n1 = float(input("Por favor digite su primer numero de la operacion: "))
#n2 = float(input("Por favor digite su segundo numero de la operacion: "))

#print("Menu de operaciones")
#print("n\Selecciona la operacion necesaria")
#print("1. Suma")
#print("2. Resta")
#print("3. Multiplicacion")
#print("4. Division")

#opcion= int (input(f"Escoge una opcion 1 / 2 / 3 / 4 / => "))

#if opcion == 1:
#    suma = float( n1 + n2  )
#    print (f"El resultado de la suma es: ", suma)
#elif opcion ==2:
##    resta = float( n1 - n2 )
#    print (f"El resultado de la resta es: ", resta)
#elif opcion ==3:
#    multiplicacion = float( n1 * n2 ) 
#    print (f"El resultado de la miltiplicacion es: ", multiplicacion)
#elif opcion == 4:
#    Division = float(n1 / n2) 
#    print(f"El resultado de la division es: ", Division)
#else:
#    print ("opcion no valida para realizar la operacion")



#print("_________________Notas________________")

#Reprobo = 0,1,2
#Aprobo = 3
#Excelente = 4,5

#try:
#    notas = float(input("por favor ingrese su nota, teniendo en cuenta el rango de calificacion 0-5 => "))
#except ValueError:
#    print("Por favor digite su nota de manera correcta.")
#else:
#    if notas <0 or notas >5:
#    print ("Nota invalida")
#    if Reprobo:
#        print ("Usted reprobó.")
#    elif Aprobo:
#        print("Usted aprobó raspando pilas.")
#    elif Excelente:
#        print("Aprobó el examen, felicidades bien echo.")
#    else:
#        print ("Tu nota no esta en el rango valido")



print("_________________Comparador_Numeros________________")

n1 = int(input("Por favor ingrese su primer digito => "))
n2 = int(input("Por favor ingrese su segundo digito => "))
n3 = int(input("por favor ingrese su tercer digito => "))

if n1 > n2 and n1 > n3:
   mayor = n1 
elif n2 > n1 and n2 > n3:
    mayor = n2
else:
    mayor = n3

if n1 < n2 and n1 < n3:
   menor = n1 
elif n2 < n1 and n2 <n3:
    menor = n2
else:
    menor = n3 

print ("El numero mayor es: ", mayor)
print ("El numero menor es: ", menor)




















   
    

