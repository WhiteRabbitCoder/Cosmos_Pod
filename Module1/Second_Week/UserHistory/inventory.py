"""
Inventory Management System
This module allows users to add, view, modify, and delete products in an inventory.
Each product has a name, price, and quantity.

To-Do:
- Implement modify product functionality.
- Implement general statistics functionality.
- Implement data export/import functionality.
- Improve user interface.
- Add persistent storage for products.
- Manage error handling and edge cases in enter product function.
"""

import os
import platform
from Cosmos_Pod.Module1.Utils import Validator
from Cosmos_Pod.Module1.Utils.Decorators import color

products = {}
os.environ.setdefault("TERM", "xterm-256color")

open_text = "\t" * 10


class Product:
    def __init__(self, name, price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity



def search_product(name):
    return products.get(name, None)


def clear_console():
    print("\n" * 100)
    os.system("cls" if platform.system() == "Windows" else "clear")

def enter_product():
    clear_console()
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
            view_products()

            opt = input("\nAdd another product? (y/n): ").strip().lower()
            while not (opt == "y" or opt == "n"):
                opt = input("Invalid option. Add another product? (y/n): ").strip().lower()
            if opt == "y":
                continue
            break
        except KeyboardInterrupt:
            print( color("Operation cancelled by user.", "Red"))
            break

def view_products():
    clear_console()
    if not products:
        print(open_text + "No products registered."  )
    else:
        for p in products.values():
            print(open_text + f"Name: {p.name} | Quantity: {p.quantity} | Price: {p.price} | Total: {p.price * p.quantity}"  )
    input("Press Enter to continue.")

def remove_product():
    clear_console()
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


def main_menu():
    clear_console()
    while True:
        try:
            print(open_text + "Welcome to the inventory calculator!"  )
            print(open_text + "1. Add a new product."  )
            print(open_text + "2. View added products."  )
            print(open_text + "3. Modify a product. (Work in progress)"  )
            print(open_text + "4. Delete a product."  )
            print(open_text + "5. General statistics. (Work in progress)"  )
            print(open_text + "6. Data. (Work in progress)"  )
            print(open_text + "0. Exit"  )

            menu = int(input("Please enter the desired option (0-6): ").strip())
        except ValueError:
            print(open_text + "Invalid input. Enter a number between 0 and 6."  )
            continue
        except KeyboardInterrupt:
            print(color("Exiting.", "red"))
            break

        match menu:
            case 0:
                print(color("Exiting.", "Yellow"))
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
                print(open_text + "Statistics functionality not implemented yet."  )
            case 6:
                print(open_text + "Data functionality not implemented yet."  )
            case _:
                print(open_text + "Invalid option. Try again."  )


if __name__ == "__main__":
    main_menu()
