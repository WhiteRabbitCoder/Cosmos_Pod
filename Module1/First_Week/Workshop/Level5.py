"""
Nivel 5 — Retos (Integración de todo)
Objetivo: Aplicar todos los conceptos vistos en problemas más completos.

25. Sistema de calificaciones.
26. Carrito de compras.
27. Cajero automático.
28. Gestión de estudiantes (mini base de datos).
29. Calculadora avanzada (usar funciones).
30. Agenda de contactos (lista de diccionarios).
"""
from Cosmos_Pod.Module1.Utils.Decorators import color
from Cosmos_Pod.Module1.Utils.Validator import  is_valid_name, is_positive_decimal, parse_bool, is_positive_int_str


def grade_system():
    while True:
        name = input("\n\nIngrese el nombre del estudiante: ")
        while not is_valid_name(name):
            print(color("Nombre no válido. Intenta de nuevo.", "red"))
            name = input("Ingrese el nombre del estudiante: ")
        grades = []
        while True:
            try:
                grade = input("Ingrese una calificación (o \"-1\" para terminar): ")
                if is_positive_decimal(grade):
                    grades.append(float(grade))
                elif grade == "-1":
                    break
                else:
                    print(color("Calificación no válida. Intenta de nuevo.", "red"))
            except ValueError:
                print(color("Calificación no válida. Intenta de nuevo.", "red"))
        if grades:
            average = sum(grades) / len(grades)
            print(color(f"La calificación promedio de {name} es {average:.2f}.", "green"))
        else:
            print(color("No se ingresaron calificaciones.", "yellow"))

        cont = input("¿Desea ingresar otro estudiante? (s/n): ").lower()
        if parse_bool(cont) is False:
            break

def shopping_cart():
    products = [
        {"name": "Manzana", "price": 0.5},
        {"name": "Banana", "price": 0.3},
        {"name": "Naranja", "price": 0.7},
        {"name": "Leche", "price": 1.2},
        {"name": "Pan", "price": 1.5}
    ]
    cart = []
    while True:
        print("\nProductos disponibles:")
        for idx, product in enumerate(products, start=1):
            print(color(f"{idx}. {product['name']} - ${product['price']:.2f}", "cyan"))
        choice = input("Ingrese el número del producto para agregar al carrito (o \"0\" para finalizar): ")
        try:
            choice = int(choice)
            if choice == 0:
                break
            elif 1 <= choice <= len(products):
                quantity = input("Ingrese la cantidad: ")
                while not is_positive_int_str(quantity):
                    print(color("Cantidad no válida. Intenta de nuevo.", "red"))
                    quantity = input("Ingrese la cantidad: ")
                cart.append({"product": products[choice - 1], "quantity": int(quantity)})
                print(color(f"{quantity} x {products[choice - 1]['name']} agregado al carrito.", "green"))
            else:
                print(color("Opción no válida. Intenta de nuevo.", "red"))
        except ValueError:
            print(color("Opción no válida. Intenta de nuevo.", "red"))

    if cart:
        total = sum(item['product']['price'] * item['quantity'] for item in cart)
        print(color("\nResumen del carrito:", "cyan"))
        for item in cart:
            print(color(f"{item['quantity']} x {item['product']['name']} - ${item['product']['price'] * item['quantity']:.2f}", "green"))
        print(color(f"Total a pagar: ${total:.2f}", "yellow"))
    else:
        print(color("El carrito está vacío.", "yellow"))

def atm_simulator():
    try:
        print("\n\nBienvenido al Cajero Automático")
        username = input("Ingrese su nombre de usuario: ")
        pin = input("Ingrese su PIN: ")
        users = [
            {"username": "user1", "pin": "1234", "balance": 1000.0},
            {"username": "Juan", "pin": "5678", "balance": 500.0},
            {"username": "Maria", "pin": "9101", "balance": 750.0},
            {"username": "Andres", "pin": "0000", "balance": 10000.0}
        ]
        user = next((user for user in users if user["username"] == username and user["pin"] == pin), None)
        if user:
            while True:
                print("\nOpciones:")
                print("1. Consultar saldo")
                print("2. Retirar dinero")
                print("3. Depositar dinero")
                print("4. Salir")
                choice = input("Seleccione una opción: ")
                if choice == "1":
                    print(color(f"Su saldo actual es: ${user['balance']:.2f}", "green"))
                elif choice == "2":
                    amount = input("Ingrese la cantidad a retirar: ")
                    while not is_positive_decimal(amount):
                        print(color("Cantidad no válida. Intenta de nuevo.", "red"))
                        amount = input("Ingrese la cantidad a retirar: ")
                    amount = float(amount)
                    if amount <= user["balance"]:
                        user["balance"] -= amount
                        print(color(f"Retiro exitoso. Nuevo saldo: ${user['balance']:.2f}", "green"))
                    else:
                        print(color("Fondos insuficientes.", "red"))
                elif choice == "3":
                    amount = input("Ingrese la cantidad a depositar: ")
                    while not is_positive_decimal(amount):
                        print(color("Cantidad no válida. Intenta de nuevo.", "red"))
                        amount = input("Ingrese la cantidad a depositar: ")
                    amount = float(amount)
                    user["balance"] += amount
                    print(color(f"Depósito exitoso. Nuevo saldo: ${user['balance']:.2f}", "green"))
                elif choice == "4":
                    print(color("Gracias por usar el Cajero Automático. ¡Hasta luego!", "cyan"))
                    break
                else:
                    print(color("Opción no válida. Intenta de nuevo.", "red"))
        else:
            print(color("Nombre de usuario o PIN incorrecto.", "red"))
    except KeyboardInterrupt:
        print(color("\nOperación cancelada. Saliendo del Cajero Automático.", "yellow"))

def student_management():
    students = []
    while True:
        print("\nOpciones:")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        choice = input("Seleccione una opción: ")
        match choice:
            case "1":
                name = input("Ingrese el nombre del estudiante: ")
                while not is_valid_name(name):
                    print(color("Nombre no válido. Intenta de nuevo.", "red"))
                    name = input("Ingrese el nombre del estudiante: ")
                age = input("Ingrese la edad del estudiante: ")
                while not is_positive_int_str(age):
                    print(color("Edad no válida. Intenta de nuevo.", "red"))
                    age = input("Ingrese la edad del estudiante: ")
                students.append({"name": name, "age": int(age)})
                print(color(f"Estudiante '{name}' agregado.", "green"))
            case "2":
                if students:
                    print(color("Lista de estudiantes:", "cyan"))
                    for student in students:
                        print(color(f"- {student['name']}, {student['age']} años", "green"))
                else:
                    print(color("No hay estudiantes registrados.", "yellow"))
            case "3":
                search_name = input("Ingrese el nombre del estudiante a buscar: ")
                found_students = [s for s in students if s["name"].lower() == search_name.lower()]
                if found_students:
                    for student in found_students:
                        print(color(f"Estudiante encontrado: {student['name']}, {student['age']} años", "green"))
                else:
                    print(color(f"No se encontró al estudiante '{search_name}'.", "red"))
            case "4":
                delete_name = input("Ingrese el nombre del estudiante a eliminar: ")
                students = [s for s in students if s["name"].lower() != delete_name.lower()]
                print(color(f"Estudiante '{delete_name}' eliminado si existía.", "green"))
            case "5":
                print(color("Saliendo del sistema de gestión de estudiantes. ¡Hasta luego!", "cyan"))
                break
            case _:
                print(color("Opción no válida. Intenta de nuevo.", "red"))


def advanced_calculator():
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            print(color("Error: División por cero no permitida.", "red"))
            return None
        return x / y
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma (+)")
        print("2. Resta (-)")
        print("3. Multiplicación (*)")
        print("4. División (/)")
        print("5. Salir")
        choice = input("Seleccione una operación: ")
        if choice == "5":
            print(color("Saliendo de la calculadora avanzada. ¡Hasta luego!", "cyan"))
            break
        if choice in operations:
            num1 = input("Ingrese el primer número: ")
            while not is_positive_decimal(num1):
                print(color("Número no válido. Intenta de nuevo.", "red"))
                num1 = input("Ingrese el primer número: ")
            num2 = input("Ingrese el segundo número: ")
            while not is_positive_decimal(num2):
                print(color("Número no válido. Intenta de nuevo.", "red"))
                num2 = input("Ingrese el segundo número: ")
            num1 = float(num1)
            num2 = float(num2)
            result = operations[choice](num1, num2)
            if result is not None:
                print(color(f"El resultado es: {result}", "green"))
        else:
            print(color("Opción no válida. Intenta de nuevo.", "red"))

def contact_agenda():
    contacts = []
    while True:
        print("\nOpciones:")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Buscar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")
        choice = input("Seleccione una opción: ")
        match choice:
            case "1":
                name = input("Ingrese el nombre del contacto: ")
                while not is_valid_name(name):
                    print(color("Nombre no válido. Intenta de nuevo.", "red"))
                    name = input("Ingrese el nombre del contacto: ")
                phone = input("Ingrese el número de teléfono: ")
                contacts.append({"name": name, "phone": phone})
                print(color(f"Contacto '{name}' agregado.", "green"))
            case "2":
                if contacts:
                    print(color("Lista de contactos:", "cyan"))
                    for contact in contacts:
                        print(color(f"- {contact['name']}: {contact['phone']}", "green"))
                else:
                    print(color("No hay contactos registrados.", "yellow"))
            case "3":
                search_name = input("Ingrese el nombre del contacto a buscar: ")
                found_contacts = [c for c in contacts if c["name"].lower() == search_name.lower()]
                if found_contacts:
                    for contact in found_contacts:
                        print(color(f"Contacto encontrado: {contact['name']}: {contact['phone']}", "green"))
                else:
                    print(color(f"No se encontró al contacto '{search_name}'.", "red"))
            case "4":
                delete_name = input("Ingrese el nombre del contacto a eliminar: ")
                contacts = [c for c in contacts if c["name"].lower() != delete_name.lower()]
                print(color(f"Contacto '{delete_name}' eliminado si existía.", "green"))
            case "5":
                print(color("Saliendo de la agenda de contactos. ¡Hasta luego!", "cyan"))
                break
            case _:
                print(color("Opción no válida. Intenta de nuevo.", "red"))

while True:
    print("\nSeleccione una actividad para realizar:")
    print("1. Sistema de calificaciones")
    print("2. Carrito de compras")
    print("3. Cajero automático")
    print("4. Gestión de estudiantes")
    print("5. Calculadora avanzada")
    print("6. Agenda de contactos")
    print("7. Salir")
    activity = input("Ingrese el número de la actividad: ")
    match activity:
        case "1":
            grade_system()
        case "2":
            shopping_cart()
        case "3":
            atm_simulator()
        case "4":
            student_management()
        case "5":
            advanced_calculator()
        case "6":
            contact_agenda()
        case "7":
            print(color("Saliendo del programa. ¡Hasta luego!", "cyan"))
            break
        case _:
            print(color("Opción no válida. Intenta de nuevo.", "red"))