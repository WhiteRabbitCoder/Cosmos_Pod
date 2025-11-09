"""
Nivel 1 — Fundamentos y Variables
Objetivo: Practicar tipos de datos, entrada y salida, concatenación y operaciones básicas.

1. Hola usuario: pide al usuario su nombre y edad. Luego imprime un mensaje: "Hola [nombre], tienes [edad] años."
2. Suma de dos números.
3. Área del triángulo.
4. Conversor de grados Celsius a Fahrenheit.
5. Tipo de dato: usar type() para mostrar el tipo de cada variable.
6. Edad futura: pide la edad actual y muestra cuántos años tendrá el usuario dentro de 10 años.
"""
from sqlalchemy import except_

import Module1.Utils.Decorators
from Cosmos_Pod.Module1.Utils.Validator import is_positive_int, is_positive_int_str
from Cosmos_Pod.Module1.Utils.Validator import is_valid_name

color = Module1.Utils.Decorators.color


def hello_user():
    name = input("\n\n¿Cuál es tu nombre? ")
    while not is_valid_name(name):
        print(color("Nombre no válido. Intenta de nuevo.", "red"))
        name = input("¿Cuál es tu nombre? ")
    age = input("¿Cuántos años tienes? ")
    while not is_positive_int_str(age) or int(age) > 120:
        print(color("Edad no válida. Intenta de nuevo.", "red"))
        age = input("¿Cuántos años tienes? ")
    print(color(f"Hola {name}, tienes {age} años.", "green"))





def sum_two_numbers():
    num1 = None
    num2 = None
    while not (num1 and num2):
        try:
            if not num1: num1 = float(input("\n\nIngresa el primer número: "))
            if not num2: num2 = float(input("Ingresa el segundo número: "))
            total = num1 + num2
            print(color(f"La suma de {num1} y {num2} es {total}.", "green"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def triangle_area():
    base = None
    height = None
    while not (base and height):
        try:
            if not base: base = float(input("\n\nIngresa la base del triángulo: "))
            if not height: height = float(input("Ingresa la altura del triángulo: "))
            area = (base * height) / 2
            print(color(f"El área del triángulo es {area}.", "green"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def celsius_to_fahrenheit():
    celsius = None
    while celsius is None:
        try:
            celsius = float(input("\n\nIngresa la temperatura en grados Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(color(f"{celsius}°C son {fahrenheit}°F.", "green"))
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))

def show_variable_types():
    var_int = 10
    var_float = 10.5
    var_str = "Hola"
    var_bool = True
    print(color(f"\n\nEl tipo de {var_int} es {type(var_int)}.", "green"))
    print(color(f"El tipo de {var_float} es {type(var_float)}.", "Yellow"))
    print(color(f"El tipo de '{var_str}' es {type(var_str)}.", "blue"))
    print(color(f"El tipo de {var_bool} es {type(var_bool)}.", "magenta"))

def future_age():
    try:
        age = int(input("\n\n¿Cuál es tu edad actual? "))
        while not is_positive_int(age):
            print(color("Edad no válida. Intenta de nuevo.", "red"))
            age = input("¿Cuál es tu edad actual? ")
        future = age + 10
        print(color(f"En 10 años tendrás {future} años.", "green"))
    except ValueError:
        print(color("Edad no válida. Intenta de nuevo.", "red"))

def level_one_menu():
    while True:
        print("\n\nNivel 1 - Fundamentos y Variables")
        print("1. Hola usuario")
        print("2. Suma de dos números")
        print("3. Área del triángulo")
        print("4. Conversor de grados Celsius a Fahrenheit")
        print("5. Tipo de dato")
        print("6. Edad futura")
        print("0. Salir")
        choice = input("Selecciona una opción: ")
        match choice:
            case "1":
                hello_user()
            case "2":
                sum_two_numbers()
            case "3":
                triangle_area()
            case "4":
                celsius_to_fahrenheit()
            case "5":
                show_variable_types()
            case "6":
                future_age()
            case "0":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida.")

level_one_menu()