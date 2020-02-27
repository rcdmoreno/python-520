import psycopg2
import psycopg2.extras


connection = psycopg2.connect(
    user='admin',
    password='4linux',
    host='localhost',
    port=5432,
    database='projeto'
)
cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

def create_user(name, email, password):
    cursor.execute('''

        insert into users 
            (name, email, password) 
        values
            (\'{}\',\'{}\',\'{}\')
        '''.format(name, email, password)
        )
    return connection.commit()
name = input('Qual seu nome:? ')
email = input('Digite seu e-mail:? ')
password = input('Digite sua senha:? ')

create_user(name, email, password)
