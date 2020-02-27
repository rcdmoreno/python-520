
import pymongo


client = pymongo.MongoClient()
db = client.projeto

def create_user(name, email, password):
    db.users.insert({
        'name': name,
        'email': email,
        'password': password
    })

name = input('Digite seu nome: ')
email = input('Digite seu email: ')
password = input('Digite sua senha: ')

create_user(name, email, password)