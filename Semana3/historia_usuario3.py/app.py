# app.py

from servicios import *
from archivos import *

inventario = []

while True:
    print("""
--------- MENÚ ---------
1. Agregar producto
2. Mostrar inventario
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir
------------------------
""")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        precio = input("Precio: ")
        cantidad = input("Cantidad: ")
        agregar_producto(inventario, nombre, precio, cantidad)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("Nombre del producto a buscar: ")
        p = buscar_producto(inventario, nombre)
        if p:
            print("Producto encontrado:", p)
        else:
            print("No existe.")

    elif opcion == "4":
        nombre = input("Producto a actualizar: ")
        nuevo_precio = input("Nuevo precio (Enter para no cambiar): ")
        nueva_cantidad = input("Nueva cantidad (Enter para no cambiar): ")

        actualizar_producto(
            inventario,
            nombre,
            nuevo_precio if nuevo_precio else None,
            nueva_cantidad if nueva_cantidad else None
        )

    elif opcion == "5":
        nombre = input("Producto a eliminar: ")
        eliminar_producto(inventario, nombre)

    elif opcion == "6":
        calcular_estadisticas(inventario)

    elif opcion == "7":
        ruta = "inventario.csv"   # ✔️ ya no pide ruta fea
        guardar_csv(inventario, ruta)

    elif opcion == "8":
        ruta = "inventario.csv"
        cargado, errores = cargar_csv(ruta)

        if cargado is None:
            continue

        print(f"{len(cargado)} productos cargados, {errores} filas inválidas.")

        decision = input("¿Desea sobrescribir el inventario actual? (S/N): ").upper()

        if decision == "S":
            inventario = cargado
            print("Inventario sobrescrito.")
        else:
            print("Fusionando inventarios...")
            for p in cargado:
                existente = buscar_producto(inventario, p["nombre"])
                if existente:
                    existente["cantidad"] += p["cantidad"]
                    existente["precio"] = p["precio"]
                else:
                    inventario.append(p)

        print("Carga completada.")

    elif opcion == "9":
        print("Saliendo...")
        break

    else:
        print("Opción inválida. Intente de nuevo.")