# Mini base de datos
estudiantes = {}

while True:
    print("\n1. Agregar  2. Ver  3. Buscar  4. Eliminar  5. Salir")
    opcion = input("Opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        grado = input("Grado: ")
        estudiantes[nombre] = {"edad": edad, "grado": grado}

    elif opcion == "2":
        if estudiantes:
            for n, d in estudiantes.items():
                print(f"{n}: Edad {d['edad']}, Grado {d['grado']}")
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        if nombre in estudiantes:
            d = estudiantes[nombre]
            print(f"{nombre}: Edad {d['edad']}, Grado {d['grado']}")
        else:
            print("No encontrado")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if nombre in estudiantes:
            del estudiantes[nombre]
            print("Eliminado")
        else:
            print("No encontrado")

    elif opcion == "5":
        break

    else:
        print("Opción no válida")
