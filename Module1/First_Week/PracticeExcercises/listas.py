from collections import Counter

Marcas = ["Mazda", "Masserati"]

for Marca in Marcas:
    print(Marca)

print("----------------------------------------")

Marcas.append(input("Escribe la marca que quieres agregar: "))

for Marca in Marcas:
    print(Marca)

print("----------------------------------------")
Marcas.remove("Mazda")

for Marca in Marcas:
    print(Marca)

CMarcas = Counter(Marcas)
for x, y in CMarcas.items():
    print(x, y)
