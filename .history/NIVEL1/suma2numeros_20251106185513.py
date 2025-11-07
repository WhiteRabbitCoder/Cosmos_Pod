# Se solicita al usuario que ingrese el primer número y se guarda como texto en 'numero1'
numero1 = input("Ingrese el primer número a sumar: ")

# Se solicita al usuario que ingrese el segundo número y se guarda como texto en 'numero2'
numero2 = input("Ingrese el segundo número a sumar: ")

# Se convierte el primer valor ingresado a número entero
numero_uno = int(numero1)

# Se convierte el segundo valor ingresado a número entero
numero_dos = int(numero2)

# Se realiza la suma de los dos números y se guarda el resultado en 'suma_total'
suma_total = numero_uno + numero_dos

# Se muestra el resultado de la suma en pantalla
print(f"La suma total es igual a -> {suma_total}")