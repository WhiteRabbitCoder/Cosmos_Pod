numero = 0  # Acumulador donde se irá sumando todo

while True:  # Bucle infinito hasta que el usuario escriba 0
    numeroIngresado = int(input("Ingrese un número (0 para terminar): "))

    if numeroIngresado == 0:  # Si el número es 0, termina el ciclo
        print(f"Resultado final: {numero}")
        break  # Sale del bucle

    # Si no es 0, se acumula en la variable 'numero'
    numero = numero + numeroIngresado