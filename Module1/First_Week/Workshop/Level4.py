"""
Nivel 4 — Listas y Colecciones
Objetivo: Crear, recorrer, modificar y eliminar elementos en listas.

19. Lista de frutas.
20. Agregar y eliminar frutas.
21. Buscar un elemento en la lista.
22. Lista de números y promedio.
23. Números pares: guardar solo los pares.
24. Eliminar duplicados.
"""
from collections import Counter
from Cosmos_Pod.Module1.Utils.Decorators import color
from Cosmos_Pod.Module1.Utils.Validator import is_valid_name

def fruit_list():
    fruits = ["manzana", "pera", "manzana", "uva", "pera", "pera"]
    print("Lista de frutas inicial:", color(fruits, "cyan"))
    while True:
        opc = input("Bienvenido, que desea hacer?\n"
                    "1. Agregar fruta\n"
                    "2. Mostrar frutas\n"
                    "3. Mostrar detalles de una fruta\n"
                    "4. Eliminar fruta\n"
                    "5. Eliminar frutas duplicadas.\n"
                    "0. Salir\n"
                    "Seleccione una opción: ")
        match opc:
            case "1":
                fruit_name = input("Ingrese el nombre de la fruta a agregar: ").lower()
                while not is_valid_name(fruit_name):
                    print(color("Nombre no válido. Intenta de nuevo.", "red"))
                    fruit_name = input("Ingrese el nombre de la fruta a agregar: ")
                fruits.append(fruit_name)
                print(color(f"Fruta '{fruit_name}' agregada a la lista.", "green"))
            case "2":
                if fruits:
                    print(color("Lista de frutas:", "cyan"))
                    for fruit in fruits:
                        print(color(f"- {fruit}", "green"))
                else:
                    print(color("La lista de frutas está vacía.", "yellow"))
            case "3":
                search_name = input("Ingrese el nombre de la fruta a buscar: ").lower()
                if search_name in fruits:
                    print(color(f"La fruta '{search_name}' se encuentra  {fruits.count(search_name)} repetida en la lista.", "green"))
                else:
                    print(color(f"La fruta '{search_name}' no se encuentra en la lista.", "red"))
            case "4":
                delete_name = input("Ingrese el nombre de la fruta a eliminar: ")
                if delete_name in fruits:
                    fruits.remove(delete_name)
                    print(color(f"Fruta '{delete_name}' eliminada de la lista.", "green"))
                else:
                    print(color(f"La fruta '{delete_name}' no se encuentra en la lista.", "red"))
            case "5":
                aux_fruits = []
                if len(fruits) > 1 and len(fruits) == len(set(fruits)):
                    print(color("No existen frutas duplicadas.", "cyan"))
                else:
                    for x, y in Counter(fruits).items():
                        if x not in aux_fruits:
                            aux_fruits.append(x)
                            print(color(f"Se eliminaron los duplicados de la fruta: {x}", "green"))
                    fruits = aux_fruits
            case "0":
                print(color("Saliendo del programa. ¡Hasta luego!", "cyan"))
                break
            case _:
                print(color("Opción no válida. Intenta de nuevo.", "red"))

def number_list_average():
    numbers = []
    times = None
    while times is None:
        try:
            times = int(input("\n\n¿Cuántos números deseas ingresar? "))
            if times <= 0:
                print(color("El número debe ser mayor que 0. Intenta de nuevo.", "red"))
                times = None
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
    for i in range(times):
        num = None
        while num is None:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numbers.append(num)
            except ValueError:
                print(color("Número no válido. Intenta de nuevo.", "red"))
    average = sum(numbers) / len(numbers)
    print(color(f"El promedio de los números ingresados es {average}.", "green"))

def even_number_list():
    numbers = []
    even_numbers = []
    times = None
    while times is None:
        try:
            times = int(input("\n\n¿Cuántos números deseas ingresar? "))
            if times <= 0:
                print(color("El número debe ser mayor que 0. Intenta de nuevo.", "red"))
                times = None
        except ValueError:
            print(color("Número no válido. Intenta de nuevo.", "red"))
    for i in range(times):
        num = None
        while num is None:
            try:
                num = int(input(f"Ingrese el número {i+1}: "))
                numbers.append(num)
                if num % 2 == 0:
                    even_numbers.append(num)
            except ValueError:
                print(color("Número no válido. Intenta de nuevo.", "red"))
    print(color(f"Números pares ingresados: {even_numbers}", "green"))

def level_four_menu():
    while True:
        print("\n\nNivel 4 - Listas y Colecciones")
        print("1. Lista de frutas (Agregar, eliminar, buscar y eliminar duplicados)")
        print("2. Promedio de una lista de números")
        print("3. Números pares de una lista")
        print("0. Salir")
        choice = input("Selecciona una opción: ")
        match choice:
            case "1":
                fruit_list()
            case "2":
                number_list_average()
            case "3":
                even_number_list()
            case "0":
                print(color("Saliendo del programa. ¡Hasta luego!", "yellow"))
                break
            case _:
                print(color("Opción no válida. Intenta de nuevo.", "red"))

level_four_menu()