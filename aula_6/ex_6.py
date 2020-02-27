import pymongo


client = pymongo.MongoClient()
db = client.projeto

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

def find_user_by_email(email):
    return db.users.find_one({
        'email': email
    })

user = find_user_by_email(email)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo errado aconteceu')