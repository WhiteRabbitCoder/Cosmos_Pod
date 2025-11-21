def promedio(arr):
    return sum(arr)/len(arr)

def duplicados(arr):
    arr_aux = []
    for i in arr:
        if not(i in arr_aux):
            arr_aux.append(i) 
    return arr_aux

notas = [1,2,4,4,5,5,5]
print(f"El promedio es: {promedio(notas)}")
print(f"Las notas sin duplicado son: {duplicados(notas)}")
for i in range(-1, -len(notas),-1):
    print(notas[i])

notas_reverse = []
notas_reverse = notas.reverse()
print(notas.reverse())
#print(f"La lista en reversa es {notas_reverse}")



