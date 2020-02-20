def mapa(numero):
    return numero * 2 if numero % 2 == 0 else numero * 3 

def meu_mapa(lista):
    return list(map(mapa, lista))

lista = [1, 2, 3 , 4, 5]
lista_final = meu_mapa(lista)
print(lista)
print(lista_final)