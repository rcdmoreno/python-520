
def calcular_media(lista_de_notas):
    resultado = 0
    contador = 0
    for nota in lista_de_notas:
        resultado = resultado + nota
        contador = contador + 1
    return resultado / contador
 
notas = [1,8, 10,5,8,9,14,25,68,8]

media = calcular_media(notas)

print(media)