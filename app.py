#Estructura basica de una api
#*****************************************************+
#from flask import Flask, jsonify   #importa el modulo de flask y jsonify

# app = Flask(__name__) #se asigna la clase flask a la variable app
# @app.route('/') #crea un endpoint
# def home(): #define una funcion home
#     return jsonify({'mensaje':'OK'}),200 #el 200 es un estatus de resultado

# app.run() #manda a ejecutar la API 
# #*****************************************************+

from flask import Flask #importa el modulo de flask y jsonify
from SRC.V1.ROUTERS import empleados,puestos

app = Flask(__name__) #se asigna la clase flask a la variable app
def page_not_found(error):
    return "NOT FOUND PAGE",404

app.register_error_handler(404,page_not_found) #metodo de flask para el manejo de errores

#blueprint
app.register_blueprint(empleados.empleados, url_prefix = '/empleados/')
app.register_blueprint(puestos.puestos, url_prefix = '/puestos/')

if __name__ == '__main__':
    app.run(debug=True) #manda a ejecutar la API 
#*****************************************************



