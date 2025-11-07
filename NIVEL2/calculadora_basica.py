#Aqui se declaran las variables
numero1 = float(input("Ingrese el primer numero a operar: "))
operacion = str(input("Ingrese la operacion que quiere realizar (+, -, *, /): "))
numero2 = float(input("Ingrese el segundo numero a operar: "))
#se empieza a verificar que operacion es
if operacion == "+":
    resultado = numero1 + numero2
    print(f"{numero1} + {numero2} = {resultado}")

elif operacion == "-":
    resultado = numero1 - numero2
    print(f"{numero1} - {numero2} = {resultado}")

elif operacion == "*":
    resultado = numero1 * numero2
    print(f"{numero1} * {numero2} = {resultado}")
#Aqui se hace un if dentro del elif para dar una advertencia y que no divida por 0
elif operacion == "/":
    if numero2 != 0:  # ⚠️ evitar división por cero
        resultado = numero1 / numero2
        print(f"{numero1} / {numero2} = {resultado}")
    else:
        print("Error: no se puede dividir entre 0.")
#este else es por si no se pone operacion diga operacion no valida
else:
    print("Operación no válida.")