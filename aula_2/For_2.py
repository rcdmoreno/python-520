lista = [
47,
80,
50,
69,
41,
50,
5,
14,
14,
88,
]

# soma de numeros pares
soma = 0
contador = 0

for numero in lista:
    if numero % 2 == 1:
        soma = soma + numero
    contador = contador + 1
media = soma / contador
print("A soma da lista: ", soma)
print("A media da lista: ", media)

linha = 1
for numero in lista:
    if numero > media:
        print("Linha:",linha, numero)
    linha = linha + 1