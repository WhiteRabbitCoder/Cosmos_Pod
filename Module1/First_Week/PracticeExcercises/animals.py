"""
print(7%2)


Animales = [
    "perro",
    "gato",
    "elefante",
    "león",
    "tigre",
    "jirafa",
    "caballo",
    "vaca",
    "oveja",
    "conejo",
]

print(Animales[5])

print(Animales[7])

print("----------------------------")

for Animal in Animales:
    print(Animal)

print("-------De 0 a 50 de 2 en 2-------------")

for i in range (0, 50, 2):
    print(i)

print("------De 100 a 0 de 5 en 5-----------")
for i in range (100, 0, -5):
    print(i)

print("-----Pares con MOD-----------")

for i in range (0, 100):
    if (i % 2) == 0: print(i)

print("-----Impares ----------")

rango = range(1, 100)

for i in rango:
    if (i % 2) != 0: print(i)

print("-----Clasificación ----------")

rango = range(0, 100, 3)

for i in rango:
    if (i % 2) != 0: print(i)

"""