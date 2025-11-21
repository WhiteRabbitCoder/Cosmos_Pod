def manejar_submenu(crear_func, agregar_func, leer_func):
    """Maneja el submenú para cualquier tipo de archivo."""
    while True:
        print("\n\n1. Crear archivo")
        print("2. Agregar a archivo")
        print("3. Leer archivo")
        print("0. Volver al menú principal")
        opc = input("Escriba la función que desea realizar: ")

        if opc == "0":
            break

        if opc not in ["1", "2", "3"]:
            print("Opción inválida. Por favor, intente de nuevo.")
            continue

        nombre_archivo = input("Ingrese el nombre del archivo: ")

        if opc == "1":
            mensaje = input("Ingrese el mensaje del archivo: ")
            print(crear_func(nombre_archivo, mensaje))
        elif opc == "2":
            mensaje = input("Ingrese el mensaje a agregar al archivo: ")
            print(agregar_func(nombre_archivo, mensaje))
        elif opc == "3":
            print(leer_func(nombre_archivo))
