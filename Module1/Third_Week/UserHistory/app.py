# ==== app.py ====

import sys
sys.path.append("../../Utils")

from services import (agregar_producto, mostrar_inventario, buscar_producto,
                      actualizar_producto, eliminar_producto, calcular_estadisticas,
                      guardar_csv, cargar_csv)
from Cosmos_Pod.Module1.Utils.Decorators import color
from Cosmos_Pod.Module1.Utils.Validator import (is_valid_name, is_positive_decimal, parse_positive_decimal,
                                                 parse_positive_int, clean_string, is_positive_int_str)


def decorar_mensaje(texto: str, simbolo: str = "-", col: str = "reset") -> str:
    """Devuelve texto decorado con borde y color."""
    linea = simbolo * max(len(texto), 40)
    return f"{linea}\n{color(texto, col)}\n{linea}"


def validar_entrada_nombre(prompt: str, inventario: dict = None, debe_existir: bool = False) -> str:
    """
    Solicita y valida un nombre de producto.
    - Si debe_existir=True, verifica que esté en inventario.
    - Si debe_existir=False, verifica que NO esté (para agregar).
    """
    while True:
        entrada = input(prompt).strip()
        if not is_valid_name(entrada):
            print(color("X Nombre inválido. Debe tener entre 1-100 caracteres y no empezar por dígito.", "red"))
            continue

        nombre = clean_string(entrada)
        if inventario is not None:
            if debe_existir and nombre not in inventario:
                print(color(f"X El producto '{nombre}' no existe en el inventario.", "red"))
                continue
            if not debe_existir and nombre in inventario:
                print(color(f"X El producto '{nombre}' ya existe.", "red"))
                continue

        return nombre


def validar_entrada_precio(prompt: str, opcional: bool = False) -> float | None:
    """Solicita y valida un precio (>0). Si opcional=True, permite Enter para omitir."""
    while True:
        entrada = input(prompt).strip()
        if opcional and not entrada:
            return None
        if not is_positive_decimal(entrada):
            print(color("X Precio inválido. Debe ser un número positivo.", "red"))
            continue
        try:
            return parse_positive_decimal(entrada)
        except ValueError as e:
            print(color(f"X {e}", "red"))


def validar_entrada_cantidad(prompt: str, opcional: bool = False) -> int | None:
    """Solicita y valida una cantidad (>0). Si opcional=True, permite Enter para omitir."""
    while True:
        entrada = input(prompt).strip()
        if opcional and not entrada:
            return None
        if not is_positive_int_str(entrada):
            print(color("X Cantidad inválida. Debe ser un entero positivo.", "red"))
            continue
        try:
            return parse_positive_int(entrada)
        except ValueError as e:
            print(color(f"X {e}", "red"))


def mostrar_menu():
    print(decorar_mensaje("MENÚ INVENTARIO", "=", "cyan"))
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Actualizar producto")
    print("5. Eliminar producto")
    print("6. Estadísticas")
    print("7. Guardar CSV")
    print("8. Cargar CSV")
    print("9. Salir")
    print("=" * 40)


def main():
    inventario = {}

    while True:
        try:
            mostrar_menu()
            opcion = input(color("Selecciona una opción (1-9): ", "yellow")).strip()

            if opcion == "1":
                print(decorar_mensaje("Agregar Producto", "-", "blue"))
                nombre = validar_entrada_nombre("Nombre del producto: ", inventario, debe_existir=False)
                precio = validar_entrada_precio("Precio: ")
                cantidad = validar_entrada_cantidad("Cantidad: ")

                if agregar_producto(inventario, nombre, precio, cantidad):
                    print(color("V Producto agregado exitosamente.", "green"))
                else:
                    print(color("X Error al agregar producto.", "red"))

            elif opcion == "2":
                print(decorar_mensaje("Inventario Actual", "-", "blue"))
                if not inventario:
                    print(color("El inventario está vacío.", "yellow"))
                else:
                    mostrar_inventario(inventario)

            elif opcion == "3":
                print(decorar_mensaje("Buscar Producto", "-", "blue"))
                if not inventario:
                    print(color("El inventario está vacío. No hay productos para buscar.", "yellow"))
                    continue
                nombre = validar_entrada_nombre("Nombre del producto: ", inventario, debe_existir=True)
                producto = buscar_producto(inventario, nombre)
                if producto:
                    print(color(f"V Encontrado: {producto.nombre} | Precio: ${producto.precio:.2f} | "
                               f"Cantidad: {producto.cantidad} | Subtotal: ${producto.calcular_subtotal():.2f}", "green"))
                else:
                    # Esta comprobación es redundante si validar_entrada_nombre funciona bien, pero es segura.
                    print(color("X Producto no encontrado.", "yellow"))

            elif opcion == "4":
                print(decorar_mensaje("Actualizar Producto", "-", "blue"))
                if not inventario:
                    print(color("El inventario está vacío. No hay productos para actualizar.", "yellow"))
                    continue
                nombre = validar_entrada_nombre("Nombre del producto: ", inventario, debe_existir=True)
                nuevo_precio = validar_entrada_precio("Nuevo precio (Enter para omitir): ", opcional=True)
                nueva_cantidad = validar_entrada_cantidad("Nueva cantidad (Enter para omitir): ", opcional=True)

                if actualizar_producto(inventario, nombre, nuevo_precio, nueva_cantidad):
                    print(color("V Producto actualizado.", "green"))
                else:
                    print(color("X Error al actualizar. No se proporcionaron nuevos datos.", "red"))

            elif opcion == "5":
                print(decorar_mensaje("Eliminar Producto", "-", "blue"))
                if not inventario:
                    print(color("El inventario está vacío. No hay productos para eliminar.", "yellow"))
                    continue
                nombre = validar_entrada_nombre("Nombre del producto: ", inventario, debe_existir=True)
                if eliminar_producto(inventario, nombre):
                    print(color("V Producto eliminado.", "green"))
                else:
                    print(color("X Error al eliminar.", "red"))

            elif opcion == "6":
                if not inventario:
                    print(color("El inventario está vacío. No se pueden calcular estadísticas.", "yellow"))
                    continue
                stats = calcular_estadisticas(inventario)
                print(decorar_mensaje("ESTADÍSTICAS DEL INVENTARIO", "=", "magenta"))
                print(f"Unidades totales: {color(str(stats['unidades_totales']), 'cyan')}")
                print(f"Valor total: {color(f"${stats['valor_total']:.2f}", 'green')}")
                if stats["producto_mas_caro"]:
                    n, pr = stats["producto_mas_caro"]
                    print(f"Producto más caro: {color(n, 'yellow')} (${pr:.2f})")
                if stats["producto_mayor_stock"]:
                    n, c = stats["producto_mayor_stock"]
                    print(f"Mayor stock: {color(n, 'yellow')} ({c} uds)")
                print("=" * 40)

            elif opcion == "7":
                print(decorar_mensaje("Guardar Inventario", "-", "blue"))
                if not inventario:
                    print(color("El inventario está vacío. No hay nada que guardar.", "yellow"))
                    continue
                archivo = input("Nombre del archivo CSV (Enter para 'inventario.csv'): ").strip()
                archivo = archivo if archivo else "inventario.csv"
                if guardar_csv(inventario, archivo):
                    print(color(f"V Inventario guardado en '{archivo}'.", "green"))
                else:
                    print(color("X Error al guardar el archivo.", "red"))

            elif opcion == "8":
                print(decorar_mensaje("Cargar Inventario", "-", "blue"))
                archivo = input("Nombre del archivo CSV (Enter para 'inventario.csv'): ").strip()
                archivo = archivo if archivo else "inventario.csv"
                exito, cantidad = cargar_csv(inventario, archivo)
                if exito:
                    print(color(f"V Se cargaron {cantidad} productos desde '{archivo}'.", "green"))
                else:
                    print(color(f"X Error al cargar '{archivo}' (no encontrado o formato inválido).", "red"))

            elif opcion == "9":
                print(decorar_mensaje("¡Hasta pronto!", "-", "blue"))
                break

            else:
                print(color("X Opción inválida. Selecciona un número del 1 al 9.", "red"))

        except KeyboardInterrupt:
            print(color("\n\nOperación cancelada por el usuario. Saliendo del programa.", "yellow"))
            break
        except Exception as e:
            print(color(f"X Error inesperado: {e}", "red"))


if __name__ == "__main__":
    main()
