import pymongo


client = pymongo.MongoClient()
db = client.projeto

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

def update_password(email, password):
    db.users.update({
        'email': email
    }, {
        '$set': {
            'password': password
        }
    })
    # sem $set ele apagar todos dados dexando somente o campo que foi passado no update
def update_password_not_SET(email, password):
    db.users.update({
        'email': email
    }, {
        'password': password
    })

update_password_not_SET(email, password)
update_password(email, password)