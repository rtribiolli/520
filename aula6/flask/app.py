from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

@app.route('/')
def index():
    mensagem = {'mensagem': 'minha primeira api rest'}
    return jsonify(mensagem)
   # return '<h1>hello world</h1>'

@app.route('/usuarios')
def usuario():
    usuarios = []
    for x in db.usuario.find():
        usuarios.append(usuario)

#    return jsonity([x for x in db.usuario.find()])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

