Menu = []

while True: 
    print("\nMenu Principal\n")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadisticas")
    print("4. Salir")

    opcion = input("Ingrese una opcion del 1 al 4: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto a agregar: ")
        cantidad = int(input("Ingrese la cantidad de productos a ingresar: "))
        precio = float(input("Ingrese el precio del producto: "))
        
        Menu.append({
            "nombre": producto,
            "cantidad": cantidad,
            "precio": precio
        })
        print("El producto fue agregado exitosamente")

    elif opcion == "2":
        if Menu:
            print("\nInventario:")
            for i in Menu:
                print(f"- {i['nombre']} | Cantidad: {i['cantidad']} | Precio: ${i['precio']}")
        else:
            print("No hay productos en el inventario")

    elif opcion == "3":
        if not Menu:
            print("No hay productos en el inventario para calcular estadísticas")
        else:
            valor_total = 0
            total_unidades = 0

            producto_mas_caro = Menu[0]
            producto_mas_barato = Menu[0]

            for p in Menu:
                # Acumular valor total del inventario
                valor_total += p["cantidad"] * p["precio"]

                # Acumular unidades totales
                total_unidades += p["cantidad"]

                # Comparar precio para encontrar el más caro
                if p["precio"] > producto_mas_caro["precio"]:
                    producto_mas_caro = p

                # Comparar precio para encontrar el más barato
                if p["precio"] < producto_mas_barato["precio"]:
                    producto_mas_barato = p

            print("\n--- Estadísticas del Inventario ---")
            print(f"Valor total del inventario: ${valor_total}")
            print(f"Total de unidades registradas: {total_unidades}")
            print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
            print(f"Producto más barato: {producto_mas_barato['nombre']} (${producto_mas_barato['precio']})")

    elif opcion == "4":
        print("Salir del programa ")
        break

    else:
        print("Opción no válida, intenta nuevamente.")