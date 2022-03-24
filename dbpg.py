import psycopg2
import psycopg2.extras

DB_HOST = 'localhost'
DB_NAME = 'proyecto3'
DB_USER = 'postgres'
DB_PASS = 'conexion'

conn = psycopg2.connect(dbname = DB_NAME,user = DB_USER,password = DB_PASS,host = DB_HOST)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

class conexion:

    def insertarestudiante(codigo,nombre,apellido,edad):
        cur.execute("CALL insertarestudiante(%s,%s,%s,%s)",(codigo,nombre,apellido,edad))
        conn.commit()

    def aditarestudiante(id,codigo,nombre,apellido,edad):
        cur.execute("CALL editarestudiante(%s,%s,%s,%s,%s)",(id,codigo,nombre,apellido,edad))
        conn.commit()

    def insertarplan(nota1,nota2,nota3,idas,idest):
        cur.execute("CALL insertarplan(%s,%s,%s,%s,%s)",(idas,idest,nota1,nota2,nota3))
        conn.commit()

    def actualiza_notas(idas,id,nota1,nota2,nota3):
        cur.execute("CALL actualizar_notas(%s,%s,%s,%s,%s)",(idas,id,nota1,nota2,nota3))
        conn.commit()

    def eliminar_pl(idest,idasig):
         cur.execute("CALL eliminar_plan(%s,%s)",(idest,idasig))
         conn.commit()   

    def eliminar_estudiante(id):
        cur.execute("CALL eliminar_estudiante(%s)",(id,))
        conn.commit()     

    def listar_asignatura():
        con = 'select * from listar_asignatura()'
        cur.execute(con)
        lista = cur.fetchall()
        return lista 

    def buscar_estudiante(id):
        con = "select * from buscar_estudiante({})".format(id)
        cur.execute(con)
        lista = cur.fetchall()
        return lista

    def buscar_plan(id):
        con = "select * from buscar_plan({})".format(int(id))
        cur.execute(con)
        lista = cur.fetchall()
        return lista

    def buscar_asignatura(id):
        con = "select * from buscar_asignatura({})".format(int(id))
        cur.execute(con)
        lista = cur.fetchall()
        return lista

    def lista_estudiante():
        con = "select * from listar_estudiantes()"
        cur.execute(con)
        lista = cur.fetchall()
        return lista

    def listar_plan(id):
        con = "select * from listar_plan({})".format(int(id))
        cur.execute(con)
        lista = cur.fetchall()
        return lista  

    def lista_auditoria():
        con = "select * from lista_auditoria()"
        cur.execute(con)
        lista = cur.fetchall()
        return lista    