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
        retorno=[]
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numeroempleado},'','','','','','','','',0,'');")
        conn.cerrar()
        for row in resultado:
            retorno.append({
                        "tnumempleado":row[0],
                        "tnombre":row[1],
                        "tappaterno":row[2],
                        "tapmaterno":row[3],
                        "tdireccion":row[4],
                        "tcodigopostal":row[5],
                        "ttelefono":row[6],
                        "tcurp":row[7],
                        "tnss":row[8],
                        "tdescripcionpuesto":row[9],
                        "testatus":row[10],
                        "tmensaje":row[11]
                    })
        return jsonify(retorno),200 #200 success
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500 #500 error
    
@empleados.route('/agregar', methods=['POST']) #endpoint agregar un empleado a la base de datos
def agregarEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numeroempleado']
        nombre=request.json['nombre']
        apellidopaterno=request.json['apellidopaterno']
        apellidomaterno=request.json['apellidomaterno']
        direccion=request.json['direccion']
        codigopostal=request.json['codigopostal']
        telefono=request.json['telefono']
        curp=request.json['curp']
        nss=request.json['nss']
        descripcionpuesto=request.json['descripcionpuesto']
        
        retorno=[]
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'{nombre}','{apellidopaterno}','{apellidomaterno}','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{descripcionpuesto},'');")
        conn.cerrar()
        
        for row in resultado:
            retorno.append({ #retornos de la funcion
                        "tnumempleado":row[0],
                        "tnombre":row[1],
                        "tappaterno":row[2],
                        "tapmaterno":row[3],
                        "tdireccion":row[4],
                        "tcodigopostal":row[5],
                        "ttelefono":row[6],
                        "tcurp":row[7],
                        "tnss":row[8],
                        "tdescripcionpuesto":row[9],
                        "testatus":row[10],
                        "tmensaje":row[11]
                    })
        return jsonify(retorno),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500    
    
@empleados.route('/modificar', methods=['PUT']) #endpoint para modificar la informacion de un empleado
def modificarEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numeroempleado']
        direccion=request.json['direccion']
        codigopostal=request.json['codigopostal']
        telefono=request.json['telefono']
        curp=request.json['curp']
        nss=request.json['nss']
        descripcionpuesto=request.json['descripcionpuesto']
        
        retorno = []
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'','','','{direccion}','{codigopostal}','{telefono}','{curp}','{nss}',{descripcionpuesto},'');")
        conn.cerrar()
        
        for row in resultado:
           retorno.append({ #retornos de la funcion
                       "tnumempleado":row[0],
                       "tnombre":row[1],
                       "tappaterno":row[2],
                       "tapmaterno":row[3],
                       "tdireccion":row[4],
                       "tcodigopostal":row[5],
                       "ttelefono":row[6],
                       "tcurp":row[7],
                       "tnss":row[8],
                       "tdescripcionpuesto":row[9],
                       "testatus":row[10],
                       "tmensaje":row[11]
                   })
        
        return jsonify(retorno),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500   
    
@empleados.route('/baja', methods=['PUT']) #endpoint para dar de baja a un empleado
def bajaEmpleado():
    try:
        opcion=request.json['opcion']
        numempleado=request.json['numeroempleado']
        causabaja=request.json['causabaja']
      
        retorno = []
        resultado=[]
        conn=conexion()
        conn.conectar()
        resultado=conn.ejecutarquery(f"select * from fnoperacionesempleados({opcion},{numempleado},'','','','','','','','',0,'{causabaja}');")
        conn.cerrar()
        
        for row in resultado:
            retorno.append({ #retornos de la funcion
                        "tnumempleado":row[0],
                        "tnombre":row[1],
                        "tappaterno":row[2],
                        "tapmaterno":row[3],
                        "tdireccion":row[4],
                        "tcodigopostal":row[5],
                        "ttelefono":row[6],
                        "tcurp":row[7],
                        "tnss":row[8],
                        "tdescripcionpuesto":row[9],
                        "testatus":row[10],
                        "tmensaje":row[11]
                    })
        
        return jsonify(retorno),200
    except Exception as ex:
        return jsonify({'mensage':str(ex)}),500  
    
