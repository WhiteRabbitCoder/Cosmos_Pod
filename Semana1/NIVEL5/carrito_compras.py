productos = {"manzana": 1000, "banano":800, "pan": 2000, "leche": 4000}

# Lista vacía para el carrito
carrito = []

while True:
    print("\nProductos disponibles:")
    for p, precio in productos.items():
        print(f"- {p}: ${precio}")

    eleccion = input("\n¿Qué producto quieres agregar? (o escribe 'acabe' para hacer el total de la compra: ").lower()

    if eleccion == "salir":
        break
    elif eleccion in productos:
        carrito.append(eleccion)
        print(f" {eleccion} agregado al carrito.")
    else:
        print("Producto no encontrado, intenta de nuevo.")

# Calcular el total
total = 0
for item in carrito:
    total += productos[item]

print("\nTu carrito:", carrito)
print(f"Total a pagar: ${total:.2f}")