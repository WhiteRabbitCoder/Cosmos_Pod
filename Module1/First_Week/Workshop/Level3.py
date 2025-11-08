"""
Nivel 3 — Bucles y Repetición
Objetivo: Dominar for y while, control de iteraciones y sumatorias.

13. Contar del 1 al 10.
14. Sumatoria del 1 al n.
15. Tabla de multiplicar.
16. Contador regresivo con while.
17. Adivina el número (usar random).
18. Sumar hasta que el usuario escriba 0.
"""
import time
from Cosmos_Pod.Module1.Utils.Decorators import color
from Cosmos_Pod.Module1.Utils.Validator import is_positive_int
import random

def count_one_to_ten():
    print("\n\nContando del 1 al 10:")
    for i in range(1, 11):
        print(color(str(i), "cyan"))

def sum_one_to_n():
    n = 0
    while n is None:
        try:
            n = int(input("\n\nIngresa un número entero positivo n: "))
            if is_positive_int(n):
                total = sum(range(1, n + 1))
                print(color(f"La sumatoria del 1 al {n} es {total}.", "green"))
            else:
                print(color("Número no válido. Intenta de nuevo.", "red"))
                n = None
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def multiplication_table():
    n = 0
    while n is None:
        try:
            n = int(input("\n\nIngresa un número entero para ver su tabla de multiplicar: "))
            if is_positive_int(n):
                print(color(f"Tabla de multiplicar del {n}:", "cyan"))
                for i in range(1, 11):
                    print(color(f"{n} x {i} = {n * i}", "green"))
            else:
                print(color("Número no válido. Intenta de nuevo.", "red"))
                n = None
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def countdown():
    n = 0
    while n is None:
        try:
            n = int(input("\n\nIngresa un número entero positivo para iniciar el conteo regresivo: "))
            if is_positive_int(n):
                print(color("Iniciando conteo regresivo:", "cyan"))
                while n > 0:
                    print(color(str(n), "green"))
                    n -= 1
                    time.sleep(1)
                print(color("¡Despegue!", "magenta"))
            else:
                print(color("Número no válido. Intenta de nuevo.", "red"))
                n = None
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def guess_the_number():
    while True:
        try:
            Min = int(input("\n\nIngresa el valor mínimo del rango: "))
            Max = int(input("Ingresa el valor máximo del rango: "))
            if Min < Max:
                break
            else:
                print(color("El valor máximo debe ser mayor que el mínimo. Intenta de nuevo.", "red"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
    secret_number = random.randint(Min, Max)
    guess = None
    while guess != secret_number:
        try:
            guess = int(input(f"Adivina el número entre {Min} y {Max}: "))
            if guess < secret_number:
                print(color("Demasiado bajo. Intenta de nuevo.", "yellow"))
            elif guess > secret_number:
                print(color("Demasiado alto. Intenta de nuevo.", "yellow"))
            else:
                print(color("¡Felicidades! ¡Adivinaste el número!", "green"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def sum_until_zero():
    total = 0
    print("\n\nIngresa números para sumar. Escribe 0 para terminar.")
    while True:
        try:
            num = float(input("Ingresa un número: "))
            if num == 0:
                break
            total += num
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
    print(color(f"La suma total es {total}.", "green"))

while True:
    print("\n\nNivel 3 - Bucles y Repetición")
    print("1. Contar del 1 al 10")
    print("2. Sumatoria del 1 al n")
    print("3. Tabla de multiplicar")
    print("4. Contador regresivo con while")
    print("5. Adivina el número")
    print("6. Sumar hasta que el usuario escriba 0")
    print("7. Salir")
    choice = input("Selecciona una opción: ")
    match choice:
        case "1":
            count_one_to_ten()
        case "2":
            sum_one_to_n()
        case "3":
            multiplication_table()
        case "4":
            countdown()
        case "5":
            guess_the_number()
        case "6":
            sum_until_zero()
        case "7":
            print(color("Saliendo del programa. ¡Hasta luego!", "yellow"))
            break
        case _:
            print(color("Opción no válida. Intenta de nuevo.", "red"))