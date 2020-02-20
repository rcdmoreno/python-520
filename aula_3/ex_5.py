#def mulipliar_por_dois(x):
#    return x * 2

def mulipliar_tudo_por_dois(x, y):
    #return list(map(mulipliar_por_dois, lista))
    # funcao com uso da lambda para funcao anonima e somente um valor
    return list(map(lambda x: x * y, lista))

lista = [1, 2]
numero = input("Digite valor do multiplicador: ")
print(lista)
lista_2 = mulipliar_tudo_por_dois(lista, int(numero))
print(lista_2)