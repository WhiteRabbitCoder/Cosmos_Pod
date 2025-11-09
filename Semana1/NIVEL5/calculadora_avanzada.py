import math

# Funciones básicas
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división entre 0"

# Funciones avanzadas
def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: número negativo"

def modulo(a, b):
    if b != 0:
        return a % b
    else:
        return "Error: división entre 0"

# Menú principal
while True:
    print("\n--- Calculadora avanzada ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Módulo")
    print("8. Salir")

    opcion = input("Elige una opción (1-8): ")

    if opcion == "8":
        print("Saliendo...")
        break

    if opcion in ["1","2","3","4","5","7"]:
        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor ingresa números válidos")
            continue

    if opcion == "1":
        print("Resultado:", suma(a, b))
    elif opcion == "2":
        print("Resultado:", resta(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicacion(a, b))
    elif opcion == "4":
        print("Resultado:", division(a, b))
    elif opcion == "5":
        print("Resultado:", potencia(a, b))
    elif opcion == "6":
        try:
            a = float(input("Ingresa un número: "))
        except ValueError:
            print("Por favor ingresa un número válido")
            continue
        print("Resultado:", raiz_cuadrada(a))
    elif opcion == "7":
        print("Resultado:", modulo(a, b))
    else:
        print("Opción no válida")
