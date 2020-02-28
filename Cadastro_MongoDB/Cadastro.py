import pymongo

client = pymongo.MongoClient()
db = client.Cadastro

def create_user(name, email, password):
    db.users.insert({
        'name': name,
        'email': email,
        'password': password
    })

def find_user_by_email(email):
    return db.users.find({
        'email': email
    })

def Listar_user():
    for user in db.users.find({},{ '_id': 0, 'name': 1, 'email': 1}):
        print(user)

def delete_user_by_name(name):
    return db.users.remove({
        'name': name
    })
    
print('1 - Cadastrar novo usuário;')
print('2 - Consultar usuário por e-mail;')
print('3 - Listar usuário Cadastrados;')
print('4 - Remover Usuario pelo nome;')
print('0 - Encerrar o Programa.\n')

opcao = input('Digite a opção desejada: ')

if int(opcao) == 0:
    print('Agradeçemos sua preferência.\n\n')

elif int(opcao) == 1:
    name = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    password = input('Digite sua senha: ')
    create_user(name, email, password)

elif opcao == 2:
    email = input('Digite seu email: ')
    print(find_user_by_email(email))

elif opcao == 3:
    user = Listar_user()

elif opcao == 4:
    name = input('Digite o nome do usuario a ser deletado: ')
    print(delete_user_by_name(name))








