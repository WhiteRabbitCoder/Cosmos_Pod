"""
Nivel 2 — Condicionales (Decisiones)
Objetivo: Comprender y aplicar estructuras if, elif, else.

7. Mayor de edad.
8. Número positivo, negativo o cero.
9. Par o impar.
10. Calculadora básica con +, -, *, /.
11. Clasificador de notas (Excelente, Aprobado, Reprobado).
12. Comparador de tres números: mayor y menor.


"""
from Cosmos_Pod.Module1.Utils.Decorators import color
from Cosmos_Pod.Module1.Utils.Validator import is_positive_int

def age_check():
    age = None
    while age is None:
        try:
            age = int(input("\n\n¿Cuántos años tienes? "))
            if is_positive_int(age) and age <= 120:
                if age >= 18:
                    print(color("Eres mayor de edad.", "green"))
                elif age >= 0:
                    print(color("Eres menor de edad.", "yellow"))
            else:
                print(color("Edad no válida. Intenta de nuevo.", "red"))
                age = None
        except ValueError:
            print(color("Edad no válida. Intenta de nuevo.", "red"))

def zero_play():
    number = None
    while number is None:
        try:
            number = float(input("\n\nIngresa un número: "))
            if number > 0:
                print(color("El número es positivo.", "green"))
            elif number < 0:
                print(color("El número es negativo.", "yellow"))
            else:
                print(color("El número es cero.", "cyan"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))


def even_odd():
    number = None
    while number is None:
        try:
            number = int(input("\n\nIngresa un número entero: "))
            if number % 2 == 0:
                print(color("El número es par.", "green"))
            else:
                print(color("El número es impar.", "yellow"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))


def basic_calculator():
    num1 = None
    num2 = None
    while not (num1 and num2):
        try:
            print("\n\nCalculadora básica")
            print("¿Qué operación deseas realizar?")
            print("1. Suma (+)")
            print("2. Resta (-)")
            print("3. Multiplicación (*)")
            print("4. División (/)")
            print("5. Salir")
            operation = int(input("Selecciona una opción: "))
            while not( 0<operation<5):
                print(color("Opción no válida. Intenta de nuevo.", "red"))
                operation = input("Selecciona una opción: ")
            if operation == "5":
                print(color("Saliendo de la calculadora.", "yellow"))
                return
            if not num1: num1 = float(input("Ingresa el primer número: "))
            if not num2: num2 = float(input("Ingresa el segundo número: "))
            match str(operation):
                case "1":
                    total = num1 + num2
                    print(color(f"La suma de {num1} y {num2} es {total}.", "green"))
                case "2":
                    total = num1 - num2
                    print(color(f"La resta de {num1} y {num2} es {total}.", "green"))
                case "3":
                    total = num1 * num2
                    print(color(f"La multiplicación de {num1} y {num2} es {total}.", "green"))
                case "4":
                    if num2 == 0:
                        print(color("Error: División por cero no permitida.", "red"))
                    else:
                        total = num1 / num2
                        print(color(f"La división de {num1} entre {num2} es {total}.", "green"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
            num1, num2 = None, None

def grade_classifier():
    grade = None
    while grade is None:
        try:
            grade = float(input("\n\nIngresa la nota (0-100): "))
            if not (0 <= grade <= 100):
                print(color("La nota debe estar entre 0 y 100. Intenta de nuevo.", "red"))
                grade = None
                continue
            if grade >= 90:
                print(color("Excelente", "green"))
            elif grade >= 60:
                print(color("Aprobado", "yellow"))
            else:
                print(color("Reprobado", "red"))
        except ValueError:
            print(color("Nota no válida. Intenta de nuevo.", "red"))

def three_number_comparator():
    print("\n\nIngresa tres números para comparar.")
    nums = []
    while len(nums) < 3:
        try:
            num = float(input(f"Ingresa el número {len(nums)+1}: "))
            nums.append(num)
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
    mayor = max(nums)
    menor = min(nums)
    print(color(f"El número mayor es {mayor}.", "green"))
    print(color(f"El número menor es {menor}.", "yellow"))


def level_two_menu():
    while True:
        print("\n\nNivel 2 - Condicionales (Decisiones)")
        print("1. Mayor de edad")
        print("2. Número positivo, negativo o cero")
        print("3. Par o impar")
        print("4. Calculadora básica con +, -, *, /")
        print("5. Clasificador de notas (Excelente, Aprobado, Reprobado)")
        print("6. Comparador de tres números: mayor y menor")
        print("0. Salir")
        choice = input("Selecciona una opción: ")
        match choice:
            case "1":
                age_check()
            case "2":
                zero_play()
            case "3":
                even_odd()
            case "4":
                basic_calculator()
            case "5":
                grade_classifier()
            case "6":
                three_number_comparator()
            case "0":
                print(color("Saliendo del programa. ¡Hasta luego!", "yellow"))
                break
            case _:
                print(color("Opción no válida. Intenta de nuevo.", "red"))

level_two_menu()
