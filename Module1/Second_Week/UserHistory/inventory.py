"""
Inventory Management System
This module allows users to add, view, modify, and delete products in an inventory.
Each product has a name, price, and quantity.

To-Do:
- Implement modify product functionality.
- Implement data export/import functionality.
- Add persistent storage for products.
- Manage error handling and edge cases in enter product function.
"""

import os
import platform

from Cosmos_Pod.Module1.Utils import Validator


open_text = " " * 30
clear_console =  "\n" * 100

class Product:
    def __init__(self, name, price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity


products = {
    "Apple": Product("Apple", 0.5, 100),
    "Banana": Product("Banana", 0.3, 150),
    "Orange": Product("Orange", 0.7, 80),
}


def search_product(name):
    return products.get(name, None)


def enter_product():
    """
    Function to enter a new product into the inventory.
    :return:
    """
    print(clear_console)
    while True:
        try:
            name = input("\n\nEnter product name: ").capitalize().strip()
            while not Validator.is_valid_name(name) or name in products:
                name = input("Invalid or already existing name. Try again: ").capitalize().strip()
            # Quantity
            while True:
                quantity_input = input("\nEnter product quantity (positive integer): ").strip()
                try:
                    quantity = int(quantity_input)
                    if quantity <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid quantity. Enter a positive integer.")

            # Price
            while True:
                p_raw = input("\nEnter product price (use comma or dot for decimals): ").strip()
                try:
                    price = float(p_raw.replace(",", "."))
                    if price <= 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid price. Enter a positive number.")


            products[name] = Product(name, price, quantity)
            print(open_text + "Product added successfully!")
            opt = input("\nAdd another product? (y/n): ").strip().lower()
            while not (opt == "y" or opt == "n"):
                opt = input("Invalid option. Add another product? (y/n): ").strip().lower()
            if opt == "y":
                continue
            break
        except KeyboardInterrupt:
            print(   "Operation cancelled by user.")
            break

def view_products():
    print(clear_console)
    if not products:
        print(open_text + "No products registered."  )
    else:
        for p in products.values():
            print(open_text + f"Name: {p.name} | Quantity: {p.quantity} | Price: {p.price} | Total: {p.price * p.quantity}"  )
    input("Press Enter to continue.")

def remove_product():
    print(clear_console)
    if not products:
        print(open_text + "No products registered."  )
    else:
        name = input("Enter the product name to delete: ").strip().capitalize()
        if name in products:
            del products[name]
            print(open_text + f"Product '{name}' deleted."  )
        else:
            print(open_text + f"Product '{name}' not found."  )
    input("Press Enter to return to the main menu.")


def gerenal_reports():
    print(clear_console)
    opc = -1
    while opc != 0:
        try:
            print(open_text + "General Reports Menu:"  )
            print(open_text + "1. Total number of products."  )
            print(open_text + "2. Total inventory value."  )
            print(open_text + "0. Return to main menu."  )
            opc = int(input("Please enter the desired option (0-2): ").strip())
            match opc:
                case 0:
                    opc = 0
                case 1:
                    print(f"Total number of products: {len(products.items())}"  )
                    input("Press Enter to continue."  )
                case 2:
                    total_value = sum(p.price * p.quantity for p in products.values())
                    print(f"Total inventory value: {total_value}"  )
                    input("Press Enter to continue."  )
        except ValueError:
            print(open_text + "Invalid input. Enter a number between 0 and 2."  )
            continue
        except KeyboardInterrupt:
            print(open_text + "Exiting to main menu."  )
            opc = 0

def main_menu():
    print(clear_console)
    while True:
        try:
            print(open_text + "Welcome to the inventory calculator!"  )
            print(open_text + "1. Add a new product."  )
            print(open_text + "2. View added products."  )
            print(open_text + "3. Modify a product. (Work in progress)"  )
            print(open_text + "4. Delete a product."  )
            print(open_text + "5. General statistics."  )
            print(open_text + "6. Data. (Work in progress)"  )
            print(open_text + "0. Exit"  )

            menu = int(input("Please enter the desired option (0-6): ").strip())
        except ValueError:
            print(open_text + "Invalid input. Enter a number between 0 and 6."  )
            continue
        except KeyboardInterrupt:
            print(open_text + "Exiting.")
            break
        match menu:
            case 0:
                print(open_text + "Exiting.")
                break
            case 1:
                enter_product()
            case 2:
                view_products()
            case 3:
                print(open_text + "Modify functionality not implemented yet."  )
            case 4:
                remove_product()
            case 5:
                gerenal_reports()
            case 6:
                print(open_text + "Data functionality not implemented yet."  )
            case _:
                print(open_text + "Invalid option. Try again."  )


if __name__ == "__main__":
    main_menu()

"""
Primera semana: 
Esta semana agregué la funcionalidad de agregar, ver y eliminar productos en un inventario. 
Cada producto tiene un nombre, precio y cantidad. 
Implementé validaciones para asegurar que los datos ingresados sean correctos. 
También dejé marcadores de posición para futuras funcionalidades como modificar productos, estadísticas generales y manejo de datos.

 
Registro de cambios - Segunda Semana
Mejoré la interfaz de usuario para que sea más clara y fácil de usar.
También, agregué un data set por defecto para facilitar las pruebas.
Encontré una redundancia en la validación del nombre del producto y en la estructura de datos usada en el mismo, que planeo optimizar en el futuro.
En las próximas semanas, planeo agregar almacenamiento persistente, mejorar el manejo de errores e implementar lógica dentro del ciclo while.
"""