from config import *
from modelo import Carro

@app.route("/listar_carros")
def listar_carros():
    # obter os carros do cadastro
    carros = db.session.query(Carro).all()
    # aplicar o método json que a classe Carro possui a cada elemento da lista
    carros_em_json = [ x.json() for x in carros ]
    # converter a lista do python para json
    resposta = jsonify(carros_em_json)
    # PERMITIR resposta para pedidos oriundos de outras tecnologias
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

# iniciar o servidor web
app.run(debug=True)    
