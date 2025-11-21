from gi.overrides.Gst import init_python

clear_console = "\n*30"

def mostar_bievenida(name:str, edad:int):
    print(f"Hola, bienvenidos! Tu nombre es {name}, y tu edad es {edad}")

def multiplicar(num1:int, num2:int):
    print(f"El resultado de la multiplicación es: {num1*num2}")

def sumar(add1:int, add2:int):
    print("El resultado de la suma es:", add1 + add2)

def primo(param):
    if param % 2 == 0:
        return f"El número {param} no es primo "
    else:
        return f"El número {param} es primo"

mostar_bievenida(input("Introduce tu nombre: "), input("Introduce tu edad: "))

sumar(int(input("Introduce el primer núnero a sumar: ")), int(input("Introduce el segundo número a sumar: ")))

multiplicar(int(input("Introduce el primer número a multiplicar: ")), int(print("Introduce el segundo número a sumar: ")))

numeroprimo1 = int(input("Introduzca su primer número: "))
numeroprimo2 = int(input("Introduzca su segundo número: "))


