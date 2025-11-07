frutas = ["manzana", "banano", "pera", "fresa"]

buscar_fruta=str(input("Ingrese la fruta que quiere buscar "))

if buscar_fruta in frutas:
    print("la manzana si esta en la lista")

else:
    print("Su fruta no esta en la lista")