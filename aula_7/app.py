import sqlalchemy
import sqlalchemy.orm

import core.db
import models.user
import models.messages

core.db.Base.metadata.create_all(
    core.db.engine
)

# variavel user = nome da pasta.arquivo.classe
user = models.user.user(
    name='Lucas',
    email='test7@test.com.br',
    password='admin'
)

session = core.db.Session()
session.add(user)
session.commit()

#semmpre que for consulta deve criar session
session = core.db.Session()
results = session.query(models.user.user).filter()
for user in results:
    #user.say_hello()
    message = models.messages.Message(
        conteudo='Minha mensagem',
        user=user.id
    )
    # print(user.id, user.name)
    session = core.db.Session()
    session.add(message)
    session.commit()