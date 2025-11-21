mascotas = {
    "perro": {"edad": 1, "nombre": "Toby"},
    "gato": {"edad": 2, "nombre": "Luna"},
    "conejo": {"edad": 3, "nombre": "Luzia"}
}

print(mascotas["gato"]["nombre"])

resultados = []

for id, informacion in mascotas.items():
    q = "luna"
    nombre = informacion.get("nombre", "").lower()
    if q in nombre:
        resultados.append((id, informacion))
print(resultados)
