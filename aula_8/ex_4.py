lista = []

def get_texto():
    texto = input('Digite um texto ou "q" para sair: ')
    if texto == 'q':
        return None
    return texto

ignorar = False
while True:
    texto = get_texto()
    if ignorar:
        ignorar = False
        continue
    if texto is None:
        break
    elif texto == 'Q':
        ignorar = True
        continue
    lista.append(texto)

print(lista)