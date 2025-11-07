import os
import platform
import Validator as Validator

products = {}
os.environ.setdefault("TERM", "xterm-256color")

open_text = "╔" + "═" * 80 + "╗\n║ "
close_text = "\n╚" + "═" * 80 + "╝"

class Product:
    def __init__(self, name, price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity



def search_product(name):
    return products.get(name, None)


def clear_console():
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
                q_raw = input("\nEnter product quantity (positive integer): ").strip()
                try:
                    quantity = int(q_raw)
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
            while (opt == "y" or opt == "n") is False:
                opt = input("Invalid option. Add another product? (y/n): ").strip().lower()
            if opt == "y":
                continue
            break

        except KeyboardInterrupt:
            print(close_text + "Operation cancelled by user.")
            break

def view_products():
    clear_console
    if not products:
        print(open_text + "No products registered." + close_text)
    else:
        for p in products.values():
            print(open_text + f"Name: {p.name} | Quantity: {p.quantity} | Price: {p.price} | Total: {p.price * p.quantity}" + close_text)
    input("Press Enter to continue.")

def remove_product():
    clear_console()
    if not products:
        print(open_text + "No products registered." + close_text)
    else:
        name = input("Enter the product name to delete: ").strip().capitalize()
        if name in products:
            del products[name]
            print(open_text + f"Product '{name}' deleted." + close_text)
        else:
            print(open_text + f"Product '{name}' not found." + close_text)
    input("Press Enter to return to the main menu.")


def main_menu():
    clear_console()
    while True:
        try:
            print(open_text + "Welcome to the inventory calculator!" + close_text)
            print(open_text + "1. Add a new product." + close_text)
            print(open_text + "2. View added products." + close_text)
            print(open_text + "3. Modify a product. (Work in progress)" + close_text)
            print(open_text + "4. Delete a product." + close_text)
            print(open_text + "5. General statistics. (Work in progress)" + close_text)
            print(open_text + "6. Data. (Work in progress)" + close_text)
            print(open_text + "0. Exit" + close_text)

            menu = int(input("Please enter the desired option (0-6): ").strip())
        except ValueError:
            print(open_text + "Invalid input. Enter a number between 1 and 6." + close_text)
            continue
        except KeyboardInterrupt:
            print(close_text + "Exiting.")
            break

        match menu:
            case 0:
                print(close_text + "Exiting.")
                break
            case 1:
                enter_product()
            case 2:
                view_products()
            case 3:
                print(open_text + "Modify functionality not implemented yet." + close_text)
            case 4:
                remove_product()
            case 5:
                print(open_text + "Statistics functionality not implemented yet." + close_text)
            case 6:
                print(open_text + "Data functionality not implemented yet." + close_text)
            case _:
                print(open_text + "Invalid option. Try again." + close_text)


if __name__ == "__main__":
    main_menu()
