from flask import Flask, jsonify, make_response


app = Flask(__name__)

from datos import datos
from datos import sinClasificar, repetido, archivo, clasificado

@app.route('/ordenar')
def ordenar():
    return make_response(jsonify({"Clasificado": clasificado, "Sin clasificar": sinClasificar}),200)


@app.route('/datos') 
def getDatos():
    return make_response(jsonify({"Datos": datos}),200)
    


if __name__ == '__main__':
    app.run(debug=True, port=4000)



