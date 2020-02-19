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

lista_secundaria = []

for numero in lista:
    if numero % 2 == 0:
        lista_secundaria = lista + [ numero * 2 ]
    else:
        lista_secundaria = lista + [ numero * 3 ]

print(lista)
print(lista_secundaria)
#print("par: ", lista_secundaria)
#print("Impar: ", lista_secundaria)
   
