# aqui podemos colocar comentarios do codigo
# Tipos primitivos
#texto = "Ricardo Moreno Gomes"
#inteiro = 27
#decimais = 1.80
# booleano = True # False

nome = input("Qual seu nome: ? ")
idade = input("Qual sua idade: ? ")
email = input("Qual seu e-mail: ? ")

if int(idade) >= 18:
    print(nome, idade, email)
    print("Seja bem vindo ao Sistema")
else:
    print("Acesso Bloqueado")

