nombre = input("Ingrese su nombre ")

notas = []
for i in range(5):
    nota = float(input(f"Ingrese su nota {i+1} porfavor :"))

    while nota < 0 or nota > 100:
        print("Error esta nota no es valida")
        nota = float(input(f"Ingrese nuevamente su nota {i+1}: "))

    notas.append(nota)
    print("Nota guardada correctamente")

print(notas)

promedio = sum(notas) / len(notas)
print(f"El promedio de sus notas es igual a {promedio}")

if promedio >= 90 and promedio <= 100:
    resultado = "Excelente"
    print("Su promedio es Excelente")

elif promedio >= 70 and promedio <= 89:
    resultado = "Aprobado"
    print("Su promedio es Aprobado")

else:
    resultado = "Reprobado"
    print("Su promedio es Reprobado")

print(f"Hola {nombre}, el promedio de tus notas es {promedio} - {resultado}")