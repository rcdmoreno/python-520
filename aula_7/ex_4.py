import sqlalchemy
import sqlalchemy.orm
import core.db
import models.user
import models.messages


def create_user(name, email, password):
    user = models.user.user(
        name=name,
        email=email,
        password=password
    )
    try:
        session = core.db.Session()
        session.add(user)
        session.commit()
    except:
        print('e-mail Duplicado')

def find_user_by_email(email):
    session = core.db.Session()
    return session.query(models.user.user).filter(
        models.user.user.email == email
    ).one()
    try:
        session = core.db.Session()
        session.add(user)
        session.commit()
    except:    
        print('E-mail Duplicado')
        exit()

name = input('Digite seu nome: ')
email = input('Digite seu e-mail: ')
password = input('Digite sua senha: ')

create_user(name, email, password)
user = find_user_by_email(email)
print(user.id)