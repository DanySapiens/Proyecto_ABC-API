from flask import Blueprint, jsonify, request
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

@puestos.route('/obtener', methods=['GET']) #endpoint para traer toda la info de un puesto activo por su id o varios con id= -1
def obtenerPuesto(): 
    try:
        opcion=request.json['opcion']
        idpuesto=request.json['idpuesto']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionespuestos({opcion},{idpuesto},'',0,0);")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500

@puestos.route('/agregar', methods=['POST']) #endpoint para agregar un puesto a la base de datos
def agregarPuesto():
    try:
        opcion=request.json['opcion']
        idpuesto=request.json['idpuesto']
        descripcion=request.json['descripcion']
        empleadoalta=request.json['empleadoalta']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionespuestos({opcion},{idpuesto},'{descripcion}',{empleadoalta},0);")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500    

@puestos.route('/modificar', methods=['PUT']) #endpoint para actualizar info de un puesto en la base de datos
def modificarPuesto():
    try:
        opcion=request.json['opcion']
        idpuesto=request.json['idpuesto']
        descripcion=request.json['descripcion']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionespuestos({opcion},{idpuesto},'{descripcion}',0,0);")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500  
    
@puestos.route('/baja', methods=['PUT']) #endpoint para actualizar info de un puesto en la base de datos y darlo de baja
def bajaPuesto():
    try:
        opcion=request.json['opcion']
        idpuesto=request.json['idpuesto']
        empleadobaja=request.json['empleadobaja']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionespuestos({opcion},{idpuesto},'',0,{empleadobaja});")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500  