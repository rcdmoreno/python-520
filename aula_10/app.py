
import threading
import modules.banco as db

if __name__ == '__main__':
    user = input('Digite seu nick: ')
    try:
        f = threading.Thread(
            target=db.consultar_messagens
        )
        f.start()
    except Exception as e:
        print('Falha ao criar Thread: {}'.format(e))
    
    while f.isAlive:
        message = input()
        db.postar_mensagem(user, message)