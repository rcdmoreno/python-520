lista = []

numero = int(input("Digite um numero: "))
#lista = lista + [ numero ]

i = 1

while i <= numero:
    if i % 2 == 0:
        lista = lista + [ i ]
    else:
        lista = lista + [ i - 1]
    i = i + 1
    print(lista)