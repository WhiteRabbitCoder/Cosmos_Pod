# Lista de contactos
agenda = []

while True:
    print("\n1. Agregar contacto")
    print("2. Ver contactos")
    print("3. Buscar contacto")
    print("4. Eliminar contacto")
    print("5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        contacto = {"nombre": nombre, "telefono": telefono, "email": email}
        agenda.append(contacto)
        print("Contacto agregado.")

    elif opcion == "2":
        if agenda:
            print("\nLista de contactos:")
            for idx, c in enumerate(agenda, 1):
                print(f"{idx}. {c['nombre']} - {c['telefono']} - {c['email']}")
        else:
            print("No hay contactos registrados.")

    elif opcion == "3":
        buscar = input("Nombre a buscar: ").lower()
        encontrados = [c for c in agenda if buscar in c["nombre"].lower()]
        if encontrados:
            for c in encontrados:
                print(f"{c['nombre']} - {c['telefono']} - {c['email']}")
        else:
            print("No se encontró el contacto.")

    elif opcion == "4":
        eliminar = input("Nombre a eliminar: ").lower()
        for c in agenda:
            if eliminar == c["nombre"].lower():
                agenda.remove(c)
                print("Contacto eliminado.")
                break
        else:
            print("No se encontró el contacto.")

    elif opcion == "5":
        print("Saliendo de la agenda...")
        break

    else:
        print("Opción no válida")
