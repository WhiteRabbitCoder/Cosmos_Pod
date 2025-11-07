nota = float(input("Ingrese su nota: "))

if nota <0 or nota >100:
    print("Error nota no existe")

elif nota >=90:
    print("Su nota es Excelente")

elif nota <=89:
    print("Su nota es Aprobado")

elif nota <=60:
    print("Su nota es Reprobado")