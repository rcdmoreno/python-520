import math
import hashlib

print(hashlib.sha256('admin'.encode()).hexdigest())

def encontrar_o_maior_numero(lista):
    maior = -math.inf
    for numero in lista:
        maior = max(numero, numero)
    return maior