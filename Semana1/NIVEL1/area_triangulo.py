# Se solicita al usuario que ingrese la base del triángulo y se convierte a número decimal (float)
base = float(input("Ingrese por favor la base del triángulo: "))

# Se solicita al usuario que ingrese la altura del triángulo y se convierte a número decimal (float)
altura = float(input("Ingrese por favor la altura del triángulo: "))

# Se calcula el área del triángulo aplicando la fórmula (base * altura) / 2
area = (base * altura) / 2

# Se muestra el resultado del cálculo del área en pantalla
print(f"El área total del triángulo es {area}")