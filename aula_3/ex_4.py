
def verifica_email(email):
    num = 0
    for letra in email:
        if letra == "@":
            num = num +1   
    return True if num == 1 else False
    
email =  input("Digite seu e-mail:? ")

email_valido = verifica_email(email)
print(email_valido)


