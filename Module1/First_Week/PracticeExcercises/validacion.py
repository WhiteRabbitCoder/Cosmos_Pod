# notas = []
#
# nombre = input("Buenas noches, introduzca su nombre: ")
#
# for i in range(5):
#     print(i)
#     nota_auxiliar = None
#     while nota_auxiliar is None:
#         try:
#             nota_auxiliar = float(input("Introduzca su nota: "))
#             if  nota_auxiliar < 0 or nota_auxiliar > 100:
#                 print("Valor invalido, vuelva a intentarlo.")
#                 nota_auxiliar = None
#         except ValueError:
#             print("Valor invalido, vuelva a intentarlo.")
#     notas.append(nota_auxiliar)
#
# for nota_auxiliar in notas:
#     print(nota_auxiliar)
from Cosmos_Pod.Module1.Utils.Validator import is_positive_decimal

numero = input("Introduzca un número: ")
if is_positive_decimal(numero):
    print("El número es permitido.")
else:
    print("No es permitido.")