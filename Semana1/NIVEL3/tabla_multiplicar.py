#se define la variable
numero=int(input("Ingrese el numero que quiere multiplicar "))
print(f"Tabla de multiplical del numero: {numero}")
#se hace un bucle para que se multiplen los numeros del 1 al 100
for i in range (1 * 100):
    resultadoMultiplicar=numero*i
    print(f"El resultado de su multiplicacion del  {numero } es {resultadoMultiplicar}")