from collections import Counter

from Cosmos_Pod.Module1.Utils.Validator import is_valid_name
from Module1.Utils.Decorators import color

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
            search_name = input("Ingrese el nombre de la fruta a buscar: ")
            if search_name in fruits:
                index = fruits.index(search_name)
                print(color(f"La fruta '{search_name}' se encuentra en la posición {index}.", "green"))
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