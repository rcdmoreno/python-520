
# Imprime os numeros de 10 ate 98 com for range
#for i in range(10,99):
#    print(i)

# Imprime os numeros de 1 ate 9 e somente para lista nunca para dicionario
lista = [1,2,3,4,5,6,7,8,9]

soma = 0
contador = 0

for numero in lista:
#    print(i)
    soma = soma + numero
    contador = contador + 1
    
media = soma / contador

print(soma)
print(contador)
print(media)
