def dividir(a, b):
    try:
        return a / b
    except:
        print('um erro ocorreu')

resultado = dividir(1, 2)
print(resultado)

resultado = dividir(1, 3)
print(resultado)

resultado = dividir(1, 0)
print(resultado)

resultado = dividir(1, 5)
print(resultado)