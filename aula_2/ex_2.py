
numero = ['0','1','2','3','4','5','6','7','8','9']

idade = input("Digite sua idade: ")
num = 0
let = 0

for letras in idade:
    if letras in numero:
        #print("Digitou um numero")
        num = num + 1
    else:
        #print("Digitou um caracter nao numerico")
        let = let + 1
print("Voce digitou quantidade de numero:",num)
print("Voce digitou quantidade de letras:",let)