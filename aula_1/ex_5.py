nome = input("Digite seu nome:? ")
idade = input("Digite sua idade:? ")
email = input("Digite seu e-mail:? ")


usuario = {
    "nome": nome,
    "idade": idade,
    "email": email
   }

print(usuario["nome"])
print(usuario["idade"])
print(usuario["email"])

idade = int(usuario["idade"])

if idade > 18:
    print("Acesso liberado, voce tem maior que 18 anos, sua idade é:", idade \n)
else:
    print("Acesso bloqueado, voce nao tem idade suficiente a sua idade é:", idade\n)    
