from datetime import datetime
from curso import Curso
from carrera import Carrera
from archivo import Archivo
from profesor import Profesor

carrera = Carrera("Tecnicatura en Programación Web", 2)
carreras = [carrera]

#prints menues
def menu():
    print("¡Bienvenido/a! al campus")
    print("1 - Ingresar como alumno")
    print("2 - Ingresar como profesor")
    print("3 - Ver Cursos")
    print("4 - Salir")

def menu_alumno():
    print("\n")
    print("1 - Matricularse a un curso")
    print("2 - Desmatricularse a un curso")
    print("3 - Ver cursos")
    print("4 - Volver al menú principal")

def menu_profesor():
    print("\n")
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3- Volver al menú principal")

#funciones validaciones ingresos

#esta funcion va a buscar en la lista estudiantes, el estudiante que tenga
#el mail ingresado, si encuentra un mail en la lista de objetos que se corresponda
#al mail ingresado me devuelve el objeto estudiante que tenga ese mail, de lo contrario nada.
def buscar_estudiante_email(email, estudiantes):
    for estudiante in estudiantes:
        if estudiante.get_email() == email:
            return estudiante
    return None

def buscar_profesor_email(email, profesores):
    for profesor in profesores:
        if profesor.get_email() == email:
            return profesor
    return None

def alta_profesor (profesores):
    print("Profesor/a no encontrado/a en la base de datos. ¿Desea darse de alta en el sistema?")
    opt_alta_profesor = input("Presione 1 si desea darse de alta en el sistema. Cualquier otra tecla para volver al menú principal: ")
    if opt_alta_profesor == "1":
        cod_ingresado = input("Por favor ingrese el código admin para darse de alta al sistema: ")
        cod_ingresado = int(cod_ingresado)
        cod_admin = Profesor.cod_admin
        opt = None
        while True: 
            if cod_ingresado == cod_admin or opt == cod_admin:
                print("Código válido.")
                print("Ingrese los siguientes datos para poder anotarse en el sistema:")
                nombre = input ("Nombre: ")
                apellido = input ("Apellido: ")
                email = input ("Email: ")
                contraseña = input ("Contraseña: ")
                título = input ("Título: ")
                año_egreso = int(input("Año de egreso de la carrera: "))
                nuevo_profesor = Profesor(nombre, apellido, email, contraseña, título, año_egreso)
                profesores.append(nuevo_profesor) 
                print("El usuario fue dado de alta con éxito!")
                break
            else:
                print ("El código admin es incorrecto. Vuelva a ingresarlo o presione 1 si desea volver al menú principal.")
                opt = input()
                if opt == "1":
                    break
                else:
                    opt = int(opt)
                    continue

#submenu alumno

def matricular_alumno(estudiante, cursos_disponibles):
    if not cursos_disponibles:
        print ("ERROR. Aún no hay cursos cargados para matricularse.\n")
    if cursos_disponibles:
        contador = 1
        print("Seleccione un curso para ver información del mismo:")
        for curso in cursos_disponibles:
            print(f"{contador} - {curso.get_nombre().title()}")
            contador += 1

        continuar = True
        while continuar:
            opt = input("Ingrese la opción de menú: ")
            if opt.isnumeric():
                opt = int(opt)
                if 1 <= opt <= len(cursos_disponibles):
                    curso_elegido = cursos_disponibles[opt - 1]
                    estudiante.matricular_en_curso(curso_elegido)
                    continuar = False
                else:
                        print("Opción no válida. Por favor, ingrese un número dentro del rango.")
            else:
                print("ERROR. Ingrese una opción numérica")

def desmatricular_alumno(estudiante, cursos_disponibles):
    if not cursos_disponibles:
        print ("ERROR. Aún no hay cursos cargados para matricularse.\n")
    if not estudiante.mis_cursos:
        print("ERROR. Aún no se encuentra matriculado a ningún curso.")
    if estudiante.mis_cursos:
        contador = 1
        print("Usted se encuentra matriculado a los siguientes cursos:")
        for curso in estudiante.mis_cursos:
            print(f"{contador} - {curso.get_nombre().title()}")
            contador += 1

        continuar = True            
        while continuar:
            opt = input("\nIngrese el curso que desea desmatricularse: ")
            if opt.isnumeric():
                opt = int(opt)
                if opt <= len(estudiante.mis_cursos):
                    curso_elegido = estudiante.mis_cursos[opt- 1]
                    estudiante.desmatricular_en_curso(curso_elegido)
                    print("Se ha registrado correctamente su desmatriculación")
                    continuar=False
                else:
                    print("Opción no válida. Por favor, ingrese un número dentro del rango.")   
            else:
                print("Opción no válida. Ingrese una opción numérica.")

def mostrar_curso_alumno(estudiante):
    if not estudiante.mis_cursos:
        print("ERROR. Aún no se encuentra matriculado a ningún curso.")
    if estudiante.mis_cursos:
        contador = 1
        print("\nUsted se encuentra matriculado a los siguientes cursos:")
        for curso in estudiante.mis_cursos:
            print(f"{contador} - {curso.get_nombre().title()}")
            contador += 1   

        continuar = True
        while continuar:                
            opt = input("\nIngrese el número de curso del que desea conocer archivos:")
            if opt.isnumeric():
                opt=int(opt)
                if opt<=len(estudiante.mis_cursos):
                    curso_elegido = estudiante.mis_cursos[opt-1]
                    print("Curso:")
                    print(f"{(curso_elegido.get_nombre().title())}")

                    if not curso_elegido.archivos:
                        print("No hay archivos subidos a este curso.")
                        continuar = False
                    else:
                        print("Archivos:")
                        archivos_ordenados = sorted(curso.archivos, key=lambda x: x.get_fecha(), reverse = True)
                        for archivo in archivos_ordenados:
                            print(f"{archivo.get_nombre()}.{archivo.get_formato()}")
                            continuar = False
                else:
                    print("Opción no válida. Por favor, ingrese un número dentro del rango.")
            else:
                    print("Opción no válida. Ingrese una opción numérica")

#submenu profesor
def dictar_curso(profesor, cursos_disponibles):
    nombre = input ("Ingrese nombre del curso que desea dictar:")
    curso = Curso(nombre, carrera.get_nombre())
    profesor.dictar_curso(curso)
    cursos_disponibles.append(curso)                   
                
def mostrar_info_curso_prof(curso_elegido):
    print("\nDatos del curso seleccionado:")
    print(f"Nombre:{curso_elegido.get_nombre()}")
    print(f"Contraseña: {curso_elegido.get_contraseña_matriculacion()}")
    print(f"Carrera: {curso_elegido.get_carrera()}")
    print(f"Código: {curso_elegido.get_codigo()}")
    cantidad_archivos=len(curso_elegido.archivos)
    print(f"Cantidad de archivos: {cantidad_archivos}")   


def mostrar_cursos_profesor(profesor):
    if not profesor.mis_cursos:
        print ("ERROR. Aún no hay cursos cargados.\n")
    else:
        contador = 1
        print("Seleccione un curso para ver información del mismo:")
        for curso in profesor.mis_cursos:
            print(f"{contador} - {curso.get_nombre().title()}")
            contador += 1

        continuar = True
        while continuar:
            opt = input("Ingrese la opción de menú: ")
            if opt.isnumeric():
                opt = int(opt)

                if 1 <= opt <= len(profesor.mis_cursos):
                    curso_elegido = profesor.mis_cursos[opt - 1]
                    mostrar_info_curso_prof(curso_elegido)
                    print("\n¿Desea agregar un archivo a este curso?")
                    opt_archivos=input("Presione 1 si desea agregar un archivo. Presione cualquier tecla para volver al submenu de profesor: ")
                    if opt_archivos== "1":
                        nombre = input ("Ingrese nombre del archivo que desea agregar: ")
                        fecha = datetime.now() #.now() me asigna fecha y hora del archivo subido. Asigna la fecha del día como pide el Tp y agrega la hora para poder ordenarlo, si existieran dos archivos del mismo día.
                        formato = input ("Ingrese el formato del archivo que desea agregar: ")
                        archivo = Archivo(nombre, fecha, formato)
                        curso_elegido.nuevo_archivo(archivo)
                        continuar= False
                    else: 
                        continuar=False
                else:
                    print("Opción no válida. Ingrese un número dentro del rango.")
            else:
                print("ERROR. Ingrese una opción numérica")

#opcion 3 menu principal

def ordenar_cursos(cursos_disponibles):
    cursos_ordenados = sorted(cursos_disponibles, key=lambda curso: curso.get_nombre())  #key lamba ayuda a ordenar la lista en base a un atributo especifico del objeto, en este caso "nombre" del objeto "curso"
    lista_ordenada = ''

    for curso in cursos_ordenados:
        nombre = curso.get_nombre().title()
        carrera = curso.get_carrera()
        linea = f"Curso: {nombre}        Carrera:{carrera}\n"
        lista_ordenada += linea

    print(lista_ordenada)
