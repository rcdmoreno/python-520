# Trabalhando com Filter

def somente_os_pares(lista):
    return list(filter(lambda x: x % 2 == 0, lista))

lista = [1,2,3,4,5,6,7,8,9,10,11]
lista_par = somente_os_pares(lista)
print("Todos numeros: ",lista)
print("Numeros Pares: ",lista_par)
