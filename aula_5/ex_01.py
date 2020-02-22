lista = []
i = 0
for i in range(1, 25):
    if i % 2 == 0:
        continue
    else:
        lista.append(i)
        lista.__len__()
        lista.sort()
print("O tamanho da lista e:", lista.__len__())    
print("Lista de Numeros Impar:", lista)