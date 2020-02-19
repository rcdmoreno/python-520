# calculadora

lista = [1,2,3,4,5,6,7,8,9,10]
multiplicador = 0
soma = 0
contador = 0

print("Tabuada do Python")
operação = input("Qual operaçãoes deseja? + - x /\n: ")

calculadora = int(input("Digite numero: "))

for numero in lista:
    if operação == "+":
        multiplicador = calculadora + numero
        print(calculadora, "+", numero, ":", multiplicador)
        contador = contador + 1
        soma = soma + multiplicador
    elif operação == "-":
        multiplicador = calculadora - numero
        print(calculadora, "-", numero, ":", multiplicador)
        contador = contador + 1
    elif operação == "x":
        multiplicador = calculadora * numero
        print(calculadora, "x", numero, ":", multiplicador)
        contador = contador + 1
    elif operação == "/":
        multiplicador = calculadora / numero
        print(calculadora, "/", numero, ":", multiplicador)
        contador = contador + 1
    else:
        print(" Tchau, você nao digitou operador!!!")
        exit()
    #         soma = soma + multiplicador
    #media = soma / contador
#print("\nA soma total dos valores são: ",soma)
#print("A média dos valores são: ",media)