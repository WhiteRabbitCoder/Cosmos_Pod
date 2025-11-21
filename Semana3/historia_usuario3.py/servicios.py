# servicios.py

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un producto al inventario.
    """
    producto = {
        "nombre": nombre,
        "precio": float(precio),
        "cantidad": int(cantidad)
    }
    inventario.append(producto)
    print(f"Producto '{nombre}' agregado exitosamente.")


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario.
    """
    if len(inventario) == 0:
        print("El inventario está vacío.")
        return
    
    print("\n--- INVENTARIO ---")
    for p in inventario:
        print(f"Nombre: {p['nombre']} | Precio: {p['precio']} | Cantidad: {p['cantidad']}")
    print("------------------\n")


def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre y lo retorna si existe.
    """
    for p in inventario:
        if p["nombre"].lower() == nombre.lower():
            return p
    return None


def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """
    Actualiza precio y/o cantidad de un producto.
    """
    producto = buscar_producto(inventario, nombre)
    if producto is None:
        print("Producto no encontrado.")
        return False

    if nuevo_precio is not None:
        producto["precio"] = float(nuevo_precio)

    if nueva_cantidad is not None:
        producto["cantidad"] = int(nueva_cantidad)

    print(f"Producto '{nombre}' actualizado con éxito.")
    return True


def eliminar_producto(inventario, nombre):
    """
    Elimina un producto si existe.
    """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        print(f"Producto '{nombre}' eliminado.")
        return True

    print("Producto no encontrado.")
    return False


def calcular_estadisticas(inventario):
    """
    Calcula unidades totales, valor total, producto más caro y el de mayor stock.
    """
    if len(inventario) == 0:
        print("No hay estadísticas porque el inventario está vacío.")
        return

    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    print("\n--- ESTADÍSTICAS ---")
    print(f"Unidades totales: {unidades_totales}")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Producto más caro: {producto_mas_caro['nombre']} (${producto_mas_caro['precio']})")
    print(f"Producto con más stock: {producto_mayor_stock['nombre']} ({producto_mayor_stock['cantidad']})")
    print("----------------------\n")