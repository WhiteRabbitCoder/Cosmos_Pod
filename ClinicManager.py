from orca.settings import keyboardLayout

from Pacientes_Constante import *
pacientes = Pacientes_constantes()

def buscar_pacientes():
    print("\n\n¿Cómo desea buscar al paciente?\n")
    opciones = None
    while opciones != "0":
        try:
            print("1. Buscar pacientes por nombre.")
            print("2. Buscar pacientes por ID.")
            print("3. Buscar pacientes por diagnostico.")
            print("0. Regresar al menú anterior. ")
            opciones = input("\nIngrese la opción que desea usar: ")
            match opciones:
                case "0":
                    break
                case "1":
                    nombre = input("Por favor, introduzca el nombre completo o parcial del paciente: ")
                    for paciente in pacientes:
                        if paciente["nombre"] == nombre or :


        except KeyboardInterrupt:
            print("Saliendo... ")
            break

def main_menu():
    print("\n\n¡Bienvenido a Clinic Manager de Riwi - By Cosmos! \n¿Qué desea hacer el día de hoy?")
    while True:
        try:
            print("1. Ingresar pacientes")
            print("2. Buscar pacientes")
            print("3. Mostrar todos los pacientes registrados.")
            print("4. Modificar pacientes. ")
            print("5. Eliminar pacientes. ")
            print("6. Exportar datos de pacientes. ")
            print("7. Importar datos de pacientes. ")
            print("0. Salir")
            menu = input("Por favor, ingrese la opción que desea (0-7): ").strip()
        except KeyboardInterrupt:
            print("Exiting.")
            break
        match menu:
            case "0":
                print("Exiting.")
                break
            case "1":
                ingresar_pacientes()
            case "2":
                buscar_pacientes()
            case "3":
                mostrar_pacientes()
            case "4":
                modificar_pacientes()
            case "5":
                eliminar_pacientes()
            case "6":
                importar_pacientes()
            case "7":
                exportar_pacientes()
            case _:
                print("Opción invalida, intente nuevamente.")

main_menu()