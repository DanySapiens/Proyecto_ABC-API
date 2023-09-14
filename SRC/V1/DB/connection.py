import psycopg2

class conexion(): #conexion a la base de datos
    
    conn=None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                database='PruebaDataBase',
                user='postgres',
                password='1234',
                port= '5433'
            )
            self.cur = self.conn.cursor()
            print("Conexión exitosa a la base de datos")
        except (Exception, psycopg2.Error) as error:
            print("Error al conectar a la base de datos:", error)

    def ejecutarquery(self,query:str):
        try:
            self.cur.execute(query)
            self.conn.commit() #guarda los cambios en base de datos
            rows = self.cur.fetchall()
            return rows
        except (Exception, psycopg2.Error) as error:
            print("Error al ejecutar la consulta:", error)

    def cerrar(self):
        try:
            self.cur.close()
            self.conn.close()
            print("Conexión cerrada")
        except (Exception, psycopg2.Error) as error:
            print("Error al cerrar la conexión:", error)