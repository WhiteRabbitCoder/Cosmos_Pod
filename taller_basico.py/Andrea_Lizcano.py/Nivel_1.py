



Nombre = input ("Por favor ingese su nombre: ")
Edad = int(input("Por favor ingrese su edad: "))
print (f"Hola",Nombre, "Tienes", Edad, "Años.")





print("_________________Suma________________")


Numero1 = int(input("Ingrese por favor su primer numero entero para sumar: "))
Numero2 = int(input ("Ingrese por favor su segundo numero entero para sumar: "))
Suma = Numero1 + Numero2
print (f"Resultado", {Suma})        




print("_________________Area_Triangulo________________")

Base = float(input("Por favor ingrese el area del triangulo: "))
Altura = float(input("Por favor ingrese la altura del triangulo: "))
Área= (1/2)*Base*Altura
print(f"El area del triangulo que solicuto es: ", Área )



print("_________________Conversor________________")

Celsius = float(input("Por favor ingrese los grados celsius a convertir: "))
Formula= Celsius*9/5+32
print ((f"La conversion solicitada es:"), {Formula})




print("_________________Type_Datos________________")

Nombre = input ("Por favor ingese su nombre: ")
Edad = int(input("Por favor ingrese su edad: "))
Altura = float(input("Por favor ingrese su altura "))
celular = int(input("por favor ingrese su numero de celular "))
Estrato = int(input("Por favor ingrese su estrato socioeconomico "))

print(type(Nombre).__name__)
print(type(Edad).__name__)
print(type(Altura).__name__)
print(type(celular).__name__)
print(type(Estrato).__name__)


print("_________________Edad_Futura________________")

Edad = int(input("por favor ingrese su edad actual: "))
Edad_2026 = Edad + 10
print ((f"Su edad en los proximos diez años será: "), {Edad_2026})

















 