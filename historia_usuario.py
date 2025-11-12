Menu = []


while True: 
    print("\nMenu Principal\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input("Ingrese una opcion del 1 al 4 ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a agregar ")
        cantidad = int(input("Ingrese la cantidad de productos a ingresar "))
        precio = float(input("Ingrese el precio del producto"))
        Menu.append({
        "nombre": producto,
        "cantidad":cantidad,
        "precio": precio
        })
        print("El producto fue agregado exitosamente")

    elif opcion == "2":
        if Menu:
            print("\n Inventario ")
            for i in Menu:
                print(f" -{i['nombre']} |  Cantidad {i['cantidad']}  |  Precio ${i['precio']}")
        else: print("No hay productos en el inventario")

    




