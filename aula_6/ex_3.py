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

email = input('Digite seu email: ')
password = input('Digite sua senha: ')

print('\n\n###### SOLUÇÃO 1 \n\n')

def find_user_by_email(email):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\';

    '''.format(email))
    return cursor.fetchone()

user = find_user_by_email(email)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo errado aconteceu')

print('\n\n###### SOLUÇÃO 2 \n\n')

def get_authenticated_user(email, password):
    cursor.execute('''

        SELECT * FROM users

        WHERE users.email = \'{}\'
        AND users.password = \'{}\';

    '''.format(email, password))
    return cursor.fetchone()

user = get_authenticated_user(email, password)

if user:
    if password == user['password']:
        print('Autenticado')
    else:
        print('Algo de errado aconteceu!!!')