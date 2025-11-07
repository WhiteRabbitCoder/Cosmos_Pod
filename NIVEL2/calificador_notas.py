#Se le pide la nota al usuario
nota = float(input("Ingrese su nota: "))
#Se verifica la nota y no puede ser superior o inferior a 100 o 0
if nota <0 or nota >100:
    print("Error nota no existe")

elif nota >=90:
    print("Su nota es Excelente")

elif nota <=89:
    print("Su nota es Aprobado")

elif nota <=60:
    print("Su nota es Reprobado")