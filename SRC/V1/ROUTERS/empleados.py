from flask import Blueprint, jsonify,request
from SRC.V1.DB.connection import conexion #importa la clase conexion de la ruta donde se encuentra

empleados = Blueprint('empleados_blueprint',__name__)
@empleados.route('/obtenerTodos', methods=['GET']) #endpoint para traer toda la info de empleados
def home(): #define una funcion de nombre home
    try:
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery("select * from tbcatempleadosprueba")
       # resultado=conn.ejecutarquery("select * from tbcatpuestosprueba")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500

@empleados.route('/obtener/<id>', methods=['GET']) #endpoint para traer toda la info de un empleado por su ID=numero de empleado
def obtenerEmpleado(id): 
    try:
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from tbcatempleadosprueba where numeroempleado = {id}")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500
    
@empleados.route('/agregar', methods=['POST']) #endpoint para traer toda la info de un empleado por su ID=numero de empleado
def agregarEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numempleado']
        nombre=request.json['nombre']
        apellidopaterno=request.json['apellidopaterno']
        apellidomaterno=request.json['apellidomaterno']
        direccion=request.json['direccion']
        codigopostal=request.json['codigopostal']
        telefono=request.json['telefono']
        curp=request.json['curp']
        nss=request.json['nss']
        descripcionpuesto=request.json['descripcionpuesto']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'{nombre}','{apellidopaterno}','{apellidomaterno}','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{descripcionpuesto},'');")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500    
    
