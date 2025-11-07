# Pedimos el nombre del producto
nombre = input("Ingrese el nombre del producto: ")

# Pedimos el precio del producto
precio = input("Ingrese el precio del producto: ")

# Mientras el precio NO sea numérico, volvemos a pedirlo
while not precio.isnumeric():
    print("Ingrese un valor numérico")
    precio = input("Ingrese el precio del producto: ")

# Convertimos el precio a número (decimal)
precioConvertido = float(precio)

# Pedimos la cantidad del producto
cantidad = input("Ingrese la cantidad del producto: ")

# Mientras la cantidad NO sea numérica, volvemos a pedirla
while not cantidad.isnumeric():
    print("Ingrese un valor numérico")
    cantidad = input("Ingrese la cantidad del producto: ")

# Convertimos la cantidad a número entero
cantidadConvertida = int(cantidad)

# Calculamos el costo total multiplicando precio por cantidad
costoTotal = precioConvertido * cantidadConvertida

# Mostramos el resultado
print(f"Producto: {nombre} | Precio Unitario: {precio} | Cantidad: {cantidad} | Total: {costoTotal}")

# ------------------------------------------------------------------------------------
# COMENTARIO GENERAL:
# Este programa pide al usuario el nombre, el precio y la cantidad de un producto.
# Verifica que el precio y la cantidad sean valores numéricos usando un ciclo while.
# Luego convierte esos valores a números (float e int), calcula el costo total
# multiplicando el precio por la cantidad, y finalmente muestra el resultado en pantalla.
# ------------------------------------------------------------------------------------
