
def calcular_media(lista):
    try:    
        soma, contador = 0, 0

        for numero in lista:
            soma , contador = soma + numero, contador + 1
        return  soma / contador
    except ZeroDivisionError:
        return none

lista = [1,2]
resultado = calcular_media(lista)
print(resultado)