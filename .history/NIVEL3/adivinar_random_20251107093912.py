import random  # Importamos la librería para generar números aleatorios

# Generamos un número secreto entre 1 y 10
numero_secreto = random.randint(1, 10)

# Pedimos al usuario que ingrese su primer intento
intento = int(input("Adivina el número (entre 1 y 10): "))

# Mientras el usuario no adivine
while intento != numero_secreto:
    # Si el número es menor que el secreto
    if intento < numero_secreto:
        print("❌ No es correcto. Intenta con un número más alto.")
    else:
        print("❌ No es correcto. Intenta con un número más bajo.")
    
    # Pedimos otro intento
    intento = int(input("Adivina de nuevo: "))

# Cuando acierta, sale del bucle y mostramos mensaje final
print(f"🎉 ¡Correcto! El número era {numero_secreto}")