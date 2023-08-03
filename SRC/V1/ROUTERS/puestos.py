from flask import Blueprint, jsonify
from SRC.V1.DB.connection import conexion #importa la clase conexion de la ruta donde se encuentra

puestos = Blueprint('puestos_blueprint',__name__)
@puestos.route('/obtenerTodos') #endpoint para traer toda la info de puestos
def home(): #define una funcion de nombre home
    try:
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery("select * from tbcatpuestosprueba")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500

@puestos.route('/obtener/<id>', methods=['GET']) #endpoint para traer toda la info de un empleado por su ID=numero de empleado
def obtenerEmpleado(id): 
    try:
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from tbcatpuestosprueba where idpuesto = {id}")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500
    
