from profesor import Profesor

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
    print("3- Ver curso")
    print("4 - Volver al menú principal")

def menu_profesor():
    print("\n")
    print("1 - Dictar curso")
    print("2 - Ver curso")
    print("3- Volver al menú principal")

def print_cursos_disponibles(cursos_disponibles): #terminar con lista de profes
    contador = 1
    print("Seleccione un curso:")
    for curso in cursos_disponibles:
        print(f"{contador} - {curso.get_nombre().title()}")
        contador += 1

def mostrar_info_curso(opt_curso_profesor,profesor):
    curso_elegido = profesor.mis_cursos[opt_curso_profesor - 1]
    print("\nDatos del curso seleccionado:")
    print(f"Nombre:{curso_elegido.get_nombre()}")
    print(f"Contraseña: {curso_elegido.get_contraseña_matriculacion()}")
    print(f"Carrera: {curso_elegido.get_carrera()}")
    print(f"Código: {curso_elegido.get_codigo()}")
    cantidad_archivos=len(curso_elegido.archivos)
    print(f"Cantidad de archivos: {cantidad_archivos}")

    
        


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

def validaciones_matricular(curso_elegido, estudiante, contraseña_ingresada) -> bool:
    if curso_elegido in estudiante.mis_cursos:
        print("El alumno ya está matriculado en este curso.")
    else:
        if curso_elegido.get_carrera == estudiante.get_carrera:
            if contraseña_ingresada == curso_elegido.get_contraseña_matriculacion:
                return True
            else:
                print("ERROR. Contraseña de matriculación incorrecta")
                return False  
        else:
            print("El alumno no se encuentra inscripto a la carrera a la cual pertenece el curso.")
            return False
        

def ordenar_cursos(cursos_disponibles):
    cursos_ordenados = sorted(cursos_disponibles, key=lambda curso: curso.get_nombre())  #key lamba ayuda a ordenar la lista en base a un atributo especifico del objeto, en este caso "nombre" del objeto "curso"
    lista_ordenada = ''

    for curso in cursos_ordenados:
        nombre = curso.get_nombre().title()
        carrera = curso.get_carrera()
        linea = f"Curso: {nombre}        Carrera:{carrera}\n"
        lista_ordenada += linea

    print(lista_ordenada)
