# ==== services.py ====

from typing import Dict, Optional
from dataclasses import dataclass
import csv


@dataclass
class Product:
    """Representa un producto con nombre, precio y cantidad."""
    nombre: str
    precio: float
    cantidad: int

    def calcular_subtotal(self) -> float:
        """Calcula el valor total del producto (precio * cantidad)."""
        return self.precio * self.cantidad


def agregar_producto(inventario: Dict[str, Product], nombre: str, precio: float, cantidad: int) -> bool:
    """
    Agrega un producto nuevo al inventario.
    Parámetros:
        inventario (dict): Diccionario {nombre: Product}.
        nombre (str): Nombre único del producto (clave).
        precio (float): Precio unitario (>= 0).
        cantidad (int): Cantidad inicial (>= 0).
    Retorno:
        bool: True si se agregó, False si ya existía.
    """
    if nombre in inventario:
        return False
    inventario[nombre] = Product(nombre, float(precio), int(cantidad))
    return True


def mostrar_inventario(inventario: Dict[str, Product]) -> None:
    """
    Imprime el inventario en formato tabular.
    Parámetros:
        inventario (dict): Diccionario de productos.
    Retorno:
        None
    """
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':<20}{'Precio':>10}{'Cantidad':>12}{'Subtotal':>12}")
    print("-" * 56)
    for producto in inventario.values():
        subtotal = producto.calcular_subtotal()
        print(f"{producto.nombre:<20}{producto.precio:>10.2f}{producto.cantidad:>12d}{subtotal:>12.2f}")


def buscar_producto(inventario: Dict[str, Product], nombre: str) -> Optional[Product]:
    """
    Busca un producto por nombre (O(1)).
    Parámetros:
        inventario (dict): Diccionario de productos.
        nombre (str): Nombre a buscar.
    Retorno:
        Product | None: El producto encontrado o None.
    """
    return inventario.get(nombre)


def actualizar_producto(inventario: Dict[str, Product], nombre: str,
                        nuevo_precio: Optional[float] = None,
                        nueva_cantidad: Optional[int] = None) -> bool:
    """
    Actualiza precio y/o cantidad de un producto existente.
    Parámetros:
        inventario (dict): Diccionario de productos.
        nombre (str): Nombre del producto a actualizar.
        nuevo_precio (float | None): Nuevo precio (si se proporciona).
        nueva_cantidad (int | None): Nueva cantidad (si se proporciona).
    Retorno:
        bool: True si se actualizó, False si no se encontró.
    """
    producto = buscar_producto(inventario, nombre)
    if not producto:
        return False
    if nuevo_precio is not None:
        producto.precio = float(nuevo_precio)
    if nueva_cantidad is not None:
        producto.cantidad = int(nueva_cantidad)
    return True


def eliminar_producto(inventario: Dict[str, Product], nombre: str) -> bool:
    """
    Elimina un producto por nombre (O(1)).
    Parámetros:
        inventario (dict): Diccionario de productos.
        nombre (str): Nombre a eliminar.
    Retorno:
        bool: True si se eliminó, False si no existía.
    """
    if nombre in inventario:
        del inventario[nombre]
        return True
    return False


def calcular_estadisticas(inventario: Dict[str, Product]) -> Dict[str, object]:
    """
    Calcula métricas del inventario.
    Parámetros:
        inventario (dict): Diccionario de productos.
    Retorno:
        dict: {
            'unidades_totales': int,
            'valor_total': float,
            'producto_mas_caro': (str, float) | None,
            'producto_mayor_stock': (str, int) | None
        }
    """
    if not inventario:
        return {
            "unidades_totales": 0,
            "valor_total": 0.0,
            "producto_mas_caro": None,
            "producto_mayor_stock": None
        }

    productos = list(inventario.values())
    unidades_totales = sum(p.cantidad for p in productos)
    valor_total = sum(p.calcular_subtotal() for p in productos)

    mas_caro = max(productos, key=lambda p: p.precio)
    mayor_stock = max(productos, key=lambda p: p.cantidad)

    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (mas_caro.nombre, mas_caro.precio),
        "producto_mayor_stock": (mayor_stock.nombre, mayor_stock.cantidad)
    }


def guardar_csv(inventario: Dict[str, Product], archivo: str = "inventario.csv") -> bool:
    """
    Guarda el inventario en un archivo CSV.
    Parámetros:
        inventario (dict): Diccionario de productos.
        archivo (str): Nombre del archivo CSV.
    Retorno:
        bool: True si se guardó exitosamente, False en caso de error.
    """
    try:
        with open(archivo, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['nombre', 'precio', 'cantidad'])  # Encabezado
            for producto in inventario.values():
                writer.writerow([producto.nombre, producto.precio, producto.cantidad])
        return True
    except Exception:
        return False


def cargar_csv(inventario: Dict[str, Product], archivo: str = "inventario.csv") -> tuple[bool, int]:
    """
    Carga productos desde un archivo CSV al inventario.
    Parámetros:
        inventario (dict): Diccionario de productos (se modificará).
        archivo (str): Nombre del archivo CSV.
    Retorno:
        tuple: (éxito: bool, productos_cargados: int)
    """
    try:
        contador = 0
        with open(archivo, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                nombre = row['nombre'].strip()
                precio = float(row['precio'])
                cantidad = int(row['cantidad'])
                # Sobrescribe si ya existe
                inventario[nombre] = Product(nombre, precio, cantidad)
                contador += 1
        return True, contador
    except FileNotFoundError:
        return False, 0
    except Exception:
        return False, 0
