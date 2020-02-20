def maior_entre_dois_numeros(a,b):
    #return a if a > b else b # operadores tenario
    if a > b:
        return a
    return b

def encontrar_maior_numero(lista_de_numeros):
    # usando a funcao max
    #for numero in lista_de_numeros:
    #    maior = max(lista_de_numeros)
    #    return maior
    maior_numero = lista_de_numeros[0]
    for numero in lista_de_numeros:
        maior_numero = maior_entre_dois_numeros(maior_numero, numero)
    return maior_numero

lista_de_numeros = [1,23,789,1212,-2,-3,-4]

maior_numero = encontrar_maior_numero(lista_de_numeros)
print(maior_numero)

