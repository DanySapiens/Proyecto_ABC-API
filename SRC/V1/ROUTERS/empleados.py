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
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500

@empleados.route('/obtener', methods=['POST']) #endpoint para traer toda la info de un empleado activo por su numero de empleado o numempl = 0 para todos
def obtenerEmpleado(): 
    try:
        opcion=request.json['opcion']
        numeroempleado=request.json['numeroempleado']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numeroempleado},'','','','','','','','',0,'');")
        # resultado=conn.ejecutarquery(f"select * from tbcatempleadosprueba where numeroempleado = {id}")
        conn.cerrar()
        return jsonify({
                        "tnumempleado":resultado[0].tnumempleado,
                        "tnombre":resultado[1],
                        "tappaterno":resultado[0],
                        "tapmaterno":resultado[0],
                        "tdireccion":resultado[0],
                        "tcodigopostal":resultado[0],
                        "ttelefono":resultado[0],
                        "tcurp":resultado[0],
                        "tnss":resultado[0],
                        "tdescripcionpuesto":resultado[0],
                        "testatus":resultado[0],
                        "tmensaje":resultado[0]
                    }),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500
    
@empleados.route('/agregar', methods=['POST']) #endpoint agregar un empleado a la base de datos
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
    
@empleados.route('/modificar', methods=['PUT']) #endpoint para modificar la informacion de un empleado
def modificarEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numempleado']
        direccion=request.json['direccion']
        codigopostal=request.json['codigopostal']
        telefono=request.json['telefono']
        curp=request.json['curp']
        nss=request.json['nss']
        descripcionpuesto=request.json['descripcionpuesto']
        
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'','','','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{descripcionpuesto},'');")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500   
    
@empleados.route('/baja', methods=['PUT']) #endpoint para dar de baja a un empleado
def bajaEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numempleado']
        causabaja=request.json['causabaja']
      
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'','','','','','','','',0,'{causabaja}');")
        conn.cerrar()
        return jsonify({'mensage':'{0}'.format(resultado)}),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500  
    
