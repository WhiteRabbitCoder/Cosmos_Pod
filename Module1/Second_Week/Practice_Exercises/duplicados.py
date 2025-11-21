lista = [1,1,1,2,3,4,4,5,5,5]

for i in range(0, len(lista)-1):
    for j in range(i+1, len(lista)):
        if j > (len(lista)-1):
            break
        elif lista[i]==lista[j]:
            del lista[j]

print(lista)