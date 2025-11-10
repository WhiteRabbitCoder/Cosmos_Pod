print("_________________Sistema de calificacion________________") 
 
#Reprobo = 0,1,2
#Aprobo = 3
#Excelente = 4,5

#try:
#    notas = float(input("por favor ingrese su nota, teniendo en cuenta el rango de calificacion 0-5 => "))
#except ValueError:
#    print("Por favor digite su nota de manera correcta.")
#else:
#    if notas <0 or notas >5:
#    print ("Nota invalida")
#    if Reprobo:
#        print ("Usted reprobó.")
#    elif Aprobo:
#        print("Usted aprobó raspando pilas.")
#    elif Excelente:
#        print("Aprobó el examen, felicidades bien echo.")
#    else:
#        print ("Tu nota no esta en el rango valido")






#print("_________________Carrito de Compras________________")

carrito = {}

while True:
    print("\n Opciones:")
    print("1. Nombre del producto")
    print("2. Precio de los productos")
    print("3. Eliminar producto")
    print("4. Productos en el carro y sus precios")
    print("5. Despedida")

    producto= input("Escribe el nombre del producto a agregar: ")
    
    if opcion == 1:
        producto = int(input("Escribe el nombre del producto a agregar: "))
        precio = float(input(f"Ingresa el precio de {producto}: "))
        carrito[producto] = precio
        print(f"{producto} se agregó al carrito con un precio de {precio}")

    elif opcion == 2:
        if carrito:
            print("Precios de los productos:")
            for producto, precio in carrito.items():
                print(f"{producto}: {precio}")
        else:
            print("El carrito está vacío.")

    elif opcion == 3:
        producto = input("Escribe el nombre del producto a eliminar: ")
        if producto in carrito:
            del carrito[producto]
            print(f"{producto} se eliminó del carrito.")
        else:
            print(f"{producto} no está en el carrito.")
    elif opcion == 4:
        if carrito:
            total = sum(carrito.values())
            print("Productos en el carrito y sus precios:")
            for producto, precio in carrito.items():
                print(f"{producto}: {precio}")
            print(f"Total a pagar: {total}")
        else:
            print("El carrito está vacío.")
    
    elif opcion == 5:
        print("Gracias por usar el carrito. ¡Hasta luego!")
        break                     # Siempre utilizamos break para finalizar el bucle 
    else:
        print("Opción inválida. Intenta de nuevo.")

