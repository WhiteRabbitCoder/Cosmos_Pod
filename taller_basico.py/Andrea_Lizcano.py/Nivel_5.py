print("_________________Sistema de calificacion________________") 
 
Reprobo = 0,1,2
Aprobo = 3
Excelente = 4,5

try:
    notas = float(input("por favor ingrese su nota, teniendo en cuenta el rango de calificacion 0-5 => "))
except ValueError:
    print("Por favor digite su nota de manera correcta.")
else:
    if notas <0 or notas >5:
     print ("Nota invalida")
    if Reprobo:
        print ("Usted reprobó.")
    elif Aprobo:
        print("Usted aprobó raspando pilas.")
    elif Excelente:
        print("Aprobó el examen, felicidades bien echo.")
    else:
        print ("Tu nota no esta en el rango valido")






print("_________________Carrito de Compras________________")

carrito = {}

while True:  # para crear un bucle que permita seleccionar más opciones del menú
    print("\nOpciones:")   # Para presentar las opciones del menú
    print("1. Agregar producto")
    print("2. Ver precios de los productos")
    print("3. Eliminar producto")
    print("4. Ver carrito y total a pagar")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        producto = input("Escribe el nombre del producto a agregar: ")
        precio = float(input(f"Ingresa el precio de {producto}: "))
        carrito[producto] = precio
        print(f"{producto} se agregó al carrito con un precio de {precio}")

    elif opcion == "2":
        if carrito:
            print("Precios de los productos:")
            for producto, precio in carrito.items():
                print(f"{producto}: {precio}")
        else:
            print("El carrito está vacío.")

    elif opcion == "3":
        producto = input("Escribe el nombre del producto a eliminar: ")
        if producto in carrito:
            del carrito[producto]
            print(f"{producto} se eliminó del carrito.")
        else:
            print(f"{producto} no está en el carrito.")

    elif opcion == "4":
        if carrito:
            total = sum(carrito.values())
            print("Productos en el carrito y sus precios:")
            for producto, precio in carrito.items():
                print(f"{producto}: {precio}")
            print(f"Total a pagar: {total}")
        else:
            print("El carrito está vacío.")

    elif opcion == "5":
        print("Gracias por usar el carrito. ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")




    
    print("_________________Cajero automatico________________") 

    saldo = 0.0  

    while True:
        print("\nOpciones:")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")
    
        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print(f"Tu saldo actual es: ${saldo}")
        
        elif opcion == "2":
            deposito = float(input("Ingresa el monto a depositar: "))
            if deposito > 0:
                saldo += deposito
                print(f"Depósito exitoso. Nuevo saldo: ${saldo}")
            else:
                print("Monto inválido. Debe ser mayor a 0.")
        
        elif opcion == "3":
            retiro = float(input("Ingresa el monto a retirar: "))
            
            if retiro <= 0:
                print("Monto inválido. Debe ser mayor a 0.") 
            elif retiro > saldo:
                print("Saldo insuficiente para realizar el retiro.")  
            else:
                saldo -= retiro
                print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
                
                ver_retiro = input("¿Quieres ver el monto retirado en pantalla? (s/n): ")
                if ver_retiro.lower() == "s":
                    print(f"El monto que retiraste es: ${retiro}")

        elif opcion == "4":
            print("Gracias por usar el cajero. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")



    
    
    
    
    print("_________________Gestión de Estudiantes________________")

    
    estudiantes = []

while True:
    print("\nOpciones:")
    print("1. Agregar estudiante")
    print("2. Ver todos los estudiantes")
    print("3. Buscar estudiante por nombre")
    print("4. Eliminar estudiante")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int(input("Ingresa la edad: "))
        promedio = float(input("Ingresa el promedio: "))
        
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "promedio": promedio
        }
        
        estudiantes.append(estudiante)
        print(f"Estudiante {nombre} agregado correctamente.")

    elif opcion == "2":
        if estudiantes:
            print("Lista de estudiantes:")
            for alumno in estudiantes:
                print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Promedio: {alumno['promedio']}")
        else:
            print("No hay estudiantes registrados.")

    elif opcion == "3":
        buscar = input("Ingresa el nombre del estudiante a buscar: ")
        encontrado = False
        for alumno in estudiantes:
            if alumno["nombre"].lower() == buscar.lower():      # .lower para que el programa me tome todo lo que escriba el usuario en minusculas y no me genere problenaa 
                print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Promedio: {alumno['promedio']}")
                encontrado = True
                break
        if not encontrado:
            print(f"Estudiante {buscar} no encontrado.")