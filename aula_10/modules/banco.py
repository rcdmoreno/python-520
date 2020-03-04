import datetime
import time
import pymongo

URL = 'mongodb://admin:58Xl25SIHPETMLdU@cluster0-shard-00-00-nstlp.mongodb.net:27017,cluster0-shard-00-01-nstlp.mongodb.net:27017,cluster0-shard-00-02-nstlp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority'

try:
    client = pymongo.MongoClient(URL)
    db = client.chat
except Exception as e:
    print('Erro de conexao: {}'.format(e))
    exit(1)
    # 0 sucesso
    # Diferente de 0 sera um erro.

def postar_mensagem(name, message):
    db.messages.insert_one({
        'name':name,
        'message':message,
        'created_at': datetime.datetime.now()
    })

def consultar_messagens():
    ultimo = [
        x for x in db.messages.find().sort('_id', pymongo.DESCENDING)
    ]
    while True:
        data = [
            x for x in db.messages.find().sort('_id', pymongo.DESCENDING)
        ]
        if data != ultimo:
            ultimo = data
            print('[{}] {} : {} \n'.format(
                data[0]['created_at'],
                data[0]['name'],
                data[0]['message'],
            ))
        time.sleep(2)