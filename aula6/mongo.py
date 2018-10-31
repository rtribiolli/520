from pymongo import MongoClient
from pprint import pprint
from datetime import datetime
from bson import ObjectId

###hash -> objectid
try:
    con = MongoClient()
    db = con['projeto']
except Exception as e:
    print('Erro: {}'.format(e))

#removendo documento
db.usuario.remove({"_id": 1})

#atualizando documento
db.usuario.update({"_id": 1},{"$set":{"sobrenome":"prata"}})

#inserindo
date = {
    "_id": 1,
    'nome':'daniel',
    'sobrenome':'prata',
    'hora': datetime.now().strftime("%d-%m-%Y %H:%M:%S")
}
db.usuario.insert(date)
# usuarios = []
# for usuario in db.usuario.find():
#     usuarios.append(usuario)

# pprint(usuarios)

usuarios = [x for x in db.usuarios.find()]