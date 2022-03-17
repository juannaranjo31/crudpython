from flask import Flask, redirect,render_template,request
import dbpg
app =  Flask(__name__)


@app.route('/')
def index():
    lista_asig = dbpg.conexion.listar_asignatura()
    lista_est = dbpg.conexion.lista_estudiante()
    return render_template('index.html',lista_as = lista_asig,lista_est = lista_est)

@app.route('/nuevo_estudiante/',methods=['GET','POST'])
def nuevo_estudiante():
    if request.method == 'POST':
        codigo = request.form['codigo']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        lista = dbpg.conexion.lista_estudiante()
        for i in lista:
            if i[1] == codigo:
                mensaje = '1'
                return render_template('nuevo_est.html',mensaje=mensaje)
        dbpg.conexion.insertarestudiante(codigo,nombre,apellido,edad)        
    return render_template('nuevo_est.html')

@app.route('/inscribir/<int:id>/',methods=['GET','POST'])
def inscribir(id):
    lista_as = dbpg.conexion.listar_asignatura()
    buscar = dbpg.conexion.listar_plan(id)
    message = ''
    if request.method == 'POST':
        asig = request.form['asignatura']
        nota_1 = request.form['nota1']
        nota_2 = request.form['nota2']
        nota_3 = request.form['nota3']
        for i in buscar:
            if i[4] == int(asig):
                dbpg.conexion.actualiza_notas(int(asig),int(id),float(nota_1),float(nota_2),float(nota_3))
                message = 'Asignatura ya inscrita, Se actualizaron las notas'
                return render_template('inscribir.html',lista_as = lista_as,message = message)    
        dbpg.conexion.insertarplan(float(nota_1),float(nota_2),float(nota_3),int(asig),int(id))
        message = 'Estudiante inscrito exitosamente'
    return render_template('inscribir.html',lista_as = lista_as,message = message)    

@app.route('/editar/<int:id>/',methods=['GET','POST'])
def editar(id):
    lista = dbpg.conexion.lista_estudiante()
    mensaje = ''
    for i in lista:
        if i[0] == id:
            lista_est = i
            if request.method == 'POST':
                codigo = i[1]
                nombre = request.form['nombre']
                apellido = request.form['apellido']
                edad = request.form['edad']
                dbpg.conexion.aditarestudiante(int(id),codigo,nombre,apellido,int(edad))
                return redirect('/')
            return render_template('editar_est.html',lista_est = lista_est)

    return render_template('editar_est.html')

@app.route('/perfil/<int:id>/')
def perfil(id):
    lista = dbpg.conexion.buscar_estudiante(id)
    lista_pl = dbpg.conexion.buscar_plan(id)
    lista_as = []
    lista_plan = dbpg.conexion.listar_plan(id)
    for i in lista_pl:
        lista_as = dbpg.conexion.buscar_asignatura(int(i[8]))
    return render_template('perfil.html',lista_pl = lista_pl,lista_as = lista_as,lista = lista,lista_plan = lista_plan)

@app.route('/eliminar_pl/<int:idest>/<int:idasig>/')
def eliminar(idest,idasig):
    id = idest
    dbpg.conexion.eliminar_pl(idest,idasig)
    message = '1'
    return redirect('/perfil/{}/'.format(id))

@app.route('/eliminar_est/<int:id>/')    
def eliminar_est(id):
    dbpg.conexion.eliminar_estudiante(id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True,port=4000)
    
