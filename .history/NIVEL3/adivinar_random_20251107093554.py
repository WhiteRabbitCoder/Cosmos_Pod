import random  # Importamos la librería random para generar números aleatorios

# Generamos un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)

# Pedimos al usuario que adivine el número
intento = int(input("Adivina el número (entre 1 y 10): "))

# Mientras el número no sea el correcto, el bucle sigue
while intento != numero_secreto:
    print("No adivinaste, intenta de nuevo")  # Mensaje si no acierta
    intento = int(input("Adivina el número (entre 1 y 10): "))  # Vuelve a pedir el número

# Si sale del bucle, significa que adivinó
print(f"🎉 ¡Correcto! El número era {numero_secreto}")